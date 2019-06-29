from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class ContactForm(forms.Form):
	name			= forms.CharField(
							widget=forms.TextInput(
								attrs= {
								"class":"form_field", 
								"id":"name", 
								'placeholder':'Your Name'
								}),label='')

	email 			= forms.EmailField(
							widget=forms.EmailInput(
								attrs= {
								"class":"form_field",
								"id":"email", 
								"placeholder":"Your Email"
								}),label='')

	phone_number 	= forms.CharField(
							widget=forms.TextInput(
								attrs= {
								"class":"form_field",
								"id":"phone_no", 
								"placeholder":"Phone Number"
								}),label='')

	message			= forms.CharField(
							widget=forms.Textarea(
								attrs= {
								"class":"form_field",
								"id":"message", 
								"placeholder":"Your Message"
								}), label='')

	def clean_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')
		if len(phone_number) < 10:
			raise forms.ValidationError("Please Enter a valid Phone Number")
		return phone_number