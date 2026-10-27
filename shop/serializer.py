from rest_framework import serializers
from .models import Product, Shop

class ShopSer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Shop
        fields = ('id', 'name', 'color', 'logo', 'user')
        read_only_fields = ('id', 'user')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'shop', 'name', 'description', 'price')
        read_only_fields = ('id',)
