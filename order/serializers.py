from rest_framework import serializers
from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ('product', 'product_count', 'product_cost')
