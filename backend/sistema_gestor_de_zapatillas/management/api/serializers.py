from rest_framework import serializers

from sistema_gestor_de_zapatillas.management.models import PointOfSale, Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class PointOfSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfSale
        fields = "__all__"
