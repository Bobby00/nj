from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from products.models import Product

from .forms import ContactForm, LoginForm, RegisterForm


# def home_page(request):
# 	return HttpResponse("<h1>Hello world!</h1>")

def home_page(request):
	queryset = Product.objects.all()
	context = {
		'object_list':queryset
	}
	return render(request, "home_page.html", context)


def about_page(request):
	return render(request, "about_page.html", {})


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form":form
	}
	# print(request.user.is_authenticated())
	if form.is_valid():
		#print(form.cleaned_data)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			if request.user.is_authenticated:
				print(True)
			else:
				print(False)
			login(request, user)
	        # Redirect to a success page.
			#context['form'] = LoginForm()
			return redirect('/')
		else:
	        # Return an 'invalid login' error message.
			print("Error, there's something wrong somewhere")
	return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form":form
	}
	if form.is_valid():
		print(form.cleaned_data)

		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		phone_number = form.cleaned_data.get('phone_number')
		password = form.cleaned_data.get('password')

		new_user = User.objects.create_user(username, email, password)
		print(new_user)

	return render(request, "auth/register.html", context)


def contact_page(request):
	contact_form = ContactForm(request.POST or None)

	context = {
		"form":contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method == "POST":
	# 	#print(request.POST)
	# 	print(request.POST.get('name'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('phone_number'))
	# 	print(request.POST.get('message')) 
	return render(request, "contact/view.html", context)