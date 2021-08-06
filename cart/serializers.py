from rest_framework import serializers
from .models import CartItem
from product.serializers import ProductSerializer


class CartSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('product', 'quantity', 'product_cost')
