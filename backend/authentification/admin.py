from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin_
from django.utils.translation import ugettext_lazy as _
from .models import User
from backend.apps.pro.models import Pro
from django.contrib.auth.models import Group

class ProInline(admin.StackedInline):
	model = Pro
	can_delete = False
	verbose_name_plural = 'Pro'

@admin.register(User)
class UserAdmin(UserAdmin_):
	fieldsets = (
		(_('Personal info'), {
			'fields': ('first_name', 'last_name', 'username', 'email', 'password', 'pro'),
		}),
		(_('Permissions'), {
			'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
		}),
		(_('Important dates'), {
			'fields': ('last_login', 'date_joined'),
		}),
	)
