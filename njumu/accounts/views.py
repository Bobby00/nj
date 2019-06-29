from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail

User = get_user_model()

def guest_register_view(request):
	form = GuestForm(request.POST or None)
	context = {
		"form":form
	}
	# print(request.user.is_authenticated())
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post or None

	if form.is_valid():
		#print(form.cleaned_data)
		email	= form.cleaned_data.get('email')
		new_guest_email = GuestEmail.objects.create(email=email)
		request.session['guest_email_id'] = new_guest_email.id
		if is_safe_url(redirect_path, request.get_host()):
			return redirect(redirect_path)
		else:
        # Redirect to a success page.
		#context['form'] = LoginForm()
			return redirect('/register/')

	return redirect('/register/')


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form":form
	}
	# print(request.user.is_authenticated())
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post or None

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
			try:
				del request.session['guest_email_id']
			except:
				pass
			login(request, user)
			if is_safe_url(redirect_path, request.get_host()):
				return redirect(redirect_path)
			else:
	        # Redirect to a success page.
			#context['form'] = LoginForm()
				return redirect('/')
		else:
	        # Return an 'invalid login' error message.
			print("Error, there's something wrong somewhere")
	return render(request, "accounts/login.html", context)


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

	return render(request, "accounts/register.html", context)
