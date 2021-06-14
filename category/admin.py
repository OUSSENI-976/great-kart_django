from django.contrib import admin
from .models import Category

#5 Affichage du slug dans admin
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('category_name',)}
	list_display = ('category_name', 'slug')


admin.site.register(Category, CategoryAdmin)
