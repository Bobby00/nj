"""njumu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path, include

from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from accounts.views import login_page, register_page, guest_register_view
from .views import home_page, about_page, contact_page
# from products.views import (product_list_view,
# 							product_detail_view,

# 							ProductDetailSlugView,

# 							ProductFeaturedListView,
# 							ProductFeaturedDetailView)

urlpatterns = [
	path('', home_page, name='home'),
	path('about/', about_page, name='about'),
	path('contact/', contact_page, name='contact'),

	path('login/', login_page, name='login'),
	path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
	path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
	path('register/guest', guest_register_view, name='guest_register'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('register/', register_page, name='register'),
	path('products/', include("products.urls")),
	path('search/', include("search.urls")),
	path('cart/', include("carts.urls")),
	# path('products/', product_list_view),
	# # path('products/<int:pk>/', product_detail_view),
	# # re_path(r'^products/(?P<slug>[\w-]+)/$', product_slug_detail_view),
	# re_path(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
	# path('featured/', ProductFeaturedListView.as_view()),
	# path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)