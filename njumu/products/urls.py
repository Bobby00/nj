

from django.urls import path, re_path

from .views import (product_list_view,
							# product_detail_view,

							ProductDetailSlugView,

							ProductFeaturedListView,
							# ProductFeaturedDetailView
							)

urlpatterns = [

	path('', product_list_view, name='list'),
	# path('products/<int:pk>/', product_detail_view),

	# re_path(r'^products/(?P<slug>[\w-]+)/$', product_slug_detail_view),
	re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),

	# path('featured/', ProductFeaturedListView.as_view()),
	# path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
]