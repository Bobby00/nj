from django.shortcuts import render, redirect

from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail

from addresses.forms import AddressForm
from addresses.models import Address

from billing.models import BillingProfile
from orders.models import Order
from products.models import Product
from .models import Cart


def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	
	# # del request.session['cart_id']
	# cart_id = request.session.get("cart_id", None)

	# # if cart_id is None: # and isinstance(cart_id, int):
	# # 	cart_obj = cart_create()
	# # 	request.session['cart_id'] = cart_obj.id
	# # else:
	# qs = Cart.objects.filter(id=cart_id)
	# if qs.count() == 1:
	# 	print("cart id exists")
	# 	cart_obj = qs.first()
	# 	if request.user.is_authenticated and cart_obj.user is None:
	# 		cart_obj.user = request.user
	# 		cart_obj.save()
	# else:
	# 	cart_obj = Cart.objects.new(user=request.user)
	# 	request.session['cart_id'] = cart_obj.id
	# # print(request.session)
	# # print(dir(request.session))
	return render(request, 'carts/home.html', {"cart": cart_obj})


def cart_update(request):
	print(request.POST)
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except ProductDoesNotExist:
			print("show message to user, product is gone?")
			return redirect('home')
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)
		request.session['cart_items'] = cart_obj.products.count()
		# return redirect(product_obj.get_absolute_url())
	return redirect('cart_home')


def checkout_home(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.products.count() == 0:
		return redirect('checkout')

	login_form = LoginForm()
	guest_form = GuestForm()
	address_form = AddressForm()

	billing_address_id = request.session.get("billing_address_id", None)
	shipping_address_id = request.session.get("shipping_address_id", None)
	# billing_address_form = AddressForm()

	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

	"ADDRESS SELECTION QUERYSET"
	address_qs = None

	if billing_profile is not None:
		if request.user.is_authenticated:
			address_qs = Address.objects.filter(billing_profile=billing_profile)

		# ''' For separation of either showing Shipping addresses or Billing addresses '''
		# shipping_address_qs = address_qs.filter(address_type='shipping')
		# billing_address_qs = address_qs.filter(address_type='billing')

		order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)

		if shipping_address_id:
			order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
			del request.session["shipping_address_id"]

		if billing_address_id:
			order_obj.billing_address_id = Address.objects.get(id=billing_address_id)
			del request.session["billing_address_id"]

		if billing_address_id or shipping_address_id:
			order_obj.save()

	'''
	Update order_obj to done, 'paid', or 'pay on delivery'
	delete cart session id 
	redirect user to a success page/view
	'''

	if request.method == 'POST':
		"Some check that order is done"
		is_done = order_obj.check_done()
		if is_done:
			order_obj.mark_paid()
			request.session['cart_items'] = 0
			del request.session['cart_id']
			return redirect('/cart/success')

	context = {
		"object"			: order_obj,
		"billing_profile"	: billing_profile,
		"login_form"		: login_form,
		"guest_form"		: guest_form,
		"address_form"		: address_form,
		"address_qs"		: address_qs
		# "billing_address_form" : billing_address_form
	}
	return render(request, "carts/checkout.html", context)
