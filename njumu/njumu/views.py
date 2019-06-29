from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from products.models import Product

from .forms import ContactForm


# def home_page(request):
# 	return HttpResponse("<h1>Hello world!</h1>"

def home_page(request):
	queryset = Product.objects.all()
	context = {
		'object_list':queryset
	}
	return render(request, "home_page.html", context)

def about_page(request):
	return render(request, "about_page.html", {})


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