from rest_framework.exceptions import ValidationError

from .models import Cart, CartItem
from product.models import Product
from django.shortcuts import get_object_or_404
from .serializers import CartItemSerializer
from decimal import Decimal


class CartApp(object):

    def __init__(self, user):
        self.cart = Cart.objects.get(user=user)
        self.items = self.cart.items.all()

    def add(self, product_id, quantity):
        product = get_object_or_404(Product, pk=product_id)
        if quantity > product.product_number:
            raise ValidationError('more than we have.')
        if self.items.filter(product=product).exists():
            item = CartItem.objects.get(cart=self.cart, product=product)
            item.quantity = quantity
            item.product_cost = Decimal(product.final_price * item.quantity)
            item.save()
        else:
            product_cost = Decimal(product.final_price * quantity)
            CartItem.objects.create(cart=self.cart, product=product, quantity=quantity, product_cost=product_cost)

    def result(self):
        return {'result': CartItemSerializer(self.items, many=True).data, 'total_price': self.total_price()}

    def clear(self):
        self.items.delete()

    def remove(self, product_id):
        item = get_object_or_404(self.items, product_id=product_id)
        item.delete()

    def total_price(self):
        total = 0
        for item in self.items:
            total += Decimal(item.product_cost)
        return total
