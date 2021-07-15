from django.urls import path
from .import views

urlpatterns = [
	path('', views.store, name='store'),
	path('category/<slug:category_slug>/', views.store, name='product_by_category'),
	path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'), ###2Url avec les 2 slug category/product
	path('search/', views.search, name='search'),
]
