import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save

from django.urls import reverse

from .utils import unique_slug_generator

# Create your models here.

class ProductManager(models.Manager):

	def featured(self):
		return self.get_queryset().filter(featured=True)

	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
		if qs.count() == 1:
			return qs.first()
		return None

class Product(models.Model):
	title 			= models.CharField(max_length=120)
	slug			= models.SlugField(blank=True, unique=True) # blank=True
	shoe_size		= models.CharField(max_length=50, null=True)
	shoe_condition 	= models.CharField(max_length=50, null=True)
	quality_score  	= models.DecimalField(decimal_places=0, max_digits=4, null=True)
	description 	= models.TextField()
	price 			= models.DecimalField(decimal_places=0, max_digits=7)
	image		   	= models.ImageField(upload_to='products/images/', null=True, blank=True)
	featured		= models.BooleanField(default=False)
	active			= models.BooleanField(default=True)
	timestamp		= models.DateTimeField(auto_now_add=True)

	objects = ProductManager()

	def get_absolute_url(self):
		# return "/products/{slug}/".format(slug=self.slug)
		return reverse("detail", kwargs={"slug": self.slug})

	def __str__(self):
		return self.title

	@property
	def name(self):
		return self.title
	


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver, sender=Product)