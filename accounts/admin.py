from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

#4 L'affichage des éléments du super User dans admin
class AccountAdmin(UserAdmin):
	list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')

	list_display_links = ('email', 'first_name', 'last_name')
	readonly_fields = ('last_login', 'date_joined')
	ordergin = ('-date_joined',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)
