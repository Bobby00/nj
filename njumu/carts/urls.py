from django.urls import path, re_path

from .views import cart_home, cart_update, checkout_home

urlpatterns = [
	path('', cart_home, name='cart_home'),
	path('checkout/', checkout_home, name='checkout'),
	path('update/', cart_update, name='update'),
	
]