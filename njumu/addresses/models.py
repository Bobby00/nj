from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPE = (
				('billing', 'Billing'),
				('shipping', 'Shipping'),
				)	

class Address(models.Model):
	billing_profile		= models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
	state_region		= models.CharField(max_length=100)
	address_type		= models.CharField(max_length=100, choices=ADDRESS_TYPE)
	delivery_address	= models.CharField(max_length=100)
	country				= models.CharField(max_length=120, default='Kenya')
	city				= models.CharField(max_length=100)

	def __str__(self):
		return str(self.billing_profile)

