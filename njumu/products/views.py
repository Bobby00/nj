from django.http import Http404
from django.views.generic import ListView, DetailView

from django.shortcuts import render, get_object_or_404

from carts.models import Cart

from .models import Product

# Create your views here.


# PRODUCTS LIST AND DETAIL VIEWS AS FUNCTION BASED VIEWS

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list':queryset
	}
	return render(request, 'products/list.html', context)



def product_detail_view(request, pk=None, *args, **kwargs):
	# try:
	# 	instance = Product.objects.get(id=pk)
	# 	instance = get_object_or_404(Product, pk=pk)
	# except Product.DoesNotExist:
	# 	print('Sorry, this product is not available')
	# 	raise Http404('Sorry, this product is not available at the moment')
	# except:
	# 	print("Uhm, we're kinda lost here, what are you looking for?")

	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404('Sorry, this product is not available at the moment')

	# print(instance)
	# qs = Product.objects.filter(id=pk)
	# if qs.exists() and qs.count() == 1:
	# 	instance = qs.first()
	# else:
	# 	raise Http404('Sorry, this product is not available at the moment')

	context = {
		'object': instance
	}

	return render(request, 'products/detail.html', context)


# PRODUCTS FEATURED LIST AND DETAIL VIEWS AS CLASS BASED VIEWS - For more robustness with the Model manager


class ProductFeaturedListView(ListView):
	template_name = "products/list.html"

		# return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
	template_name = "products/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()



class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')

		def get_queryset(self, *args, **kwargs):
			request = self.request
		try:
			instance = Product.objects.get(slug=slug)
		except Product.DoesNotExist:
			raise Http404("Not Found")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug)
			instance =  qs.first()
		except:
			raise Http404("Uhhhmmmm")

		return instance
