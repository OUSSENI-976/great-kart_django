from django.db import models
from django.urls import reverse
from category.models import Category

class Product(models.Model):
 	product_name  = models.CharField(max_length=200, unique=True)
 	slug		  = models.SlugField(max_length=200, unique=True)
 	description   = models.TextField(max_length=200, blank=True)
 	price		  = models.DecimalField(max_digits=6, decimal_places=2)
 	images		  = models.ImageField(upload_to='photos/products')
 	stock		  = models.IntegerField()
 	is_available  = models.BooleanField(default=True)
 	category 	  = models.ForeignKey(Category, on_delete=models.CASCADE)
 	create_date	  = models.DateTimeField(auto_now_add=True)
 	modefied_date = models.DateTimeField(auto_now=True)

 	####1 Obtenir l'url des produts
 	def get_url(self):
 		return reverse('product_detail', args=[self.category.slug, self.slug]) ####1-1 On utilise le champ category et son slug depuis Category(), et le slug de Product()

 	def __str__(self):
 		return self.product_name

