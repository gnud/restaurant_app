from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from restaraunt_api.models import Order, Product, Company


class ProductSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'sku',
            'name',
            'price',
            'menu',
        ]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name'
        ]


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = [
            'user',
            'company',
            'products',
        ]
