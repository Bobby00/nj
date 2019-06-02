from django.urls import path, re_path

from .views import (
						SearchProductView,
						# ProductFeaturedDetailView
					)

urlpatterns = [
	re_path(r'$', SearchProductView.as_view(), name='search'),
]