from django.contrib import admin
from .models import Industry, Employes


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    pass

@admin.register(Employes)
class EmployesAdmin(admin.ModelAdmin):
    pass

