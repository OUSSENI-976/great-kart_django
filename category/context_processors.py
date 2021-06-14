from .models import Category 

##1 Création des liens de categories -> importer la fonction menu_links settings.py
def menu_links(request):
	links = Category.objects.all()
	return dict(links=links )