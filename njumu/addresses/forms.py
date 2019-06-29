from django import forms

from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = [
			#'billing_profile',
			#'state_region',
			'address_type',
			'delivery_address',
			'country',
			'city'
		]

		widgets = {
        'delivery_address': forms.TextInput(attrs={'placeholder': 'Delivery location'}),
        'country': forms.TextInput(attrs={'placeholder': 'Country'}),
        'city': forms.TextInput(attrs={'placeholder': 'City'})
    	}

	def __init__(self, *args, **kwargs):
		super(AddressForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'cstm_brder'
			visible.label = ''
