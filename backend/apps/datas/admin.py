from django.contrib import admin
from .models import Industry, Employes, Contract, ContractTime


@admin.register(Industry, Contract, Employes)
class Admin(admin.ModelAdmin):
    pass


