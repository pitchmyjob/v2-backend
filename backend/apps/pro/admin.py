from django.contrib import admin
from .models import Pro


@admin.register(Pro)
class ProAdmin(admin.ModelAdmin):
    pass
