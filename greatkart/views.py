from django.shortcuts import render
from store.models import Product

def home(request):
	products = Product.objects.all().filter(is_available=True)
	paginate_by = 4
	context = {
		'products': products
	}
	return render(request, 'home.html', context)