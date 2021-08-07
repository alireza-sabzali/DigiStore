from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from cart.cart import CartApp
from .models import Order, OrderItem
from .serializers import OrderItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class OrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        serializer = OrderItemSerializer(order.order_items.all(), many=True)
        return Response(serializer.data)


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = CartApp(user=self.request.user)
        order = Order.objects.create(user=self.request.user)
        for item in cart.items:
            OrderItem.objects.create(order_id=order.id, product=item.product, product_count=item.quantity,
                                     product_cost=item.product_cost)
        cart.clear()
        return Response(status=status.HTTP_201_CREATED)
