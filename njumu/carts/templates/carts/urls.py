from django.urls import path, re_path

from .views import cart_home

urlpatterns = [
	path('', cart_home),
	
]