from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class GuestForm(forms.Form):
	email 			= forms.EmailField(
							widget=forms.EmailInput(
								attrs= {
								"class":"cstm_brder",
								"id":"email", 
								"placeholder":"Your Email"
								}),label='')


class LoginForm(forms.Form):
	username = forms.CharField(
								widget=forms.TextInput(
									attrs = {
									"class":"cstm_brder",
									"placeholder":"Enter Email or Username",
									"id":"name"
									}), label='')
	password = forms.CharField(
								widget=forms.PasswordInput(
									attrs = {
									"class":"cstm_brder",
									"placeholder" : "Enter Password",
									"id" : "name"
									}), label='')


class RegisterForm(forms.Form):
	username = forms.CharField(
								widget=forms.TextInput(
									attrs = {
									"class":"cstm_brder",
									"placeholder":"Enter Username"
									}), label='')
	email 			= forms.EmailField(
							widget=forms.EmailInput(
								attrs= {
								"class":"cstm_brder",
								"id":"email", 
								"placeholder":"Your Email"
								}),label='')
	# phone_number 	= forms.CharField(
	# 						widget=forms.TextInput(
	# 							attrs= {
	# 							"class":"form_field",
	# 							"id":"phone_no", 
	# 							"placeholder":"Phone Number"
	# 							}),label='')
	password = forms.CharField(
								widget=forms.PasswordInput(
									attrs = {
									"class":"cstm_brder",
									"placeholder" : "Enter Password"
									}), label='')

	password2 = forms.CharField(
								widget=forms.PasswordInput(
									attrs = {
									"class":"cstm_brder",
									"placeholder" : "Confirm Password"
									}), label='')
	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username is taken, Please try another one")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken, Please try another one")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Passwords do not match!!")
		return data	
