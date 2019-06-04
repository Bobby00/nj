from django.shortcuts import render, redirect

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
	else:
		order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
	return render(request, "carts/checkout.html", {"object": order_obj})
