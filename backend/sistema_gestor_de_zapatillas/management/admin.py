from django.contrib import admin

from sistema_gestor_de_zapatillas.management.models import PointOfSale, Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(PointOfSale)
class PointOfSaleAdmin(admin.ModelAdmin):
    pass
