from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .cart import CartApp
from .serializers import CartSerializer


class CartDetailView(APIView):

    def get(self, request):
        cart = CartApp(self.request.user)
        return Response(cart.result(), status=status.HTTP_200_OK)


class CartAddView(APIView):

    def post(self, request, product_id):
        cart = CartApp(self.request.user)
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            cart.add(product_id=product_id, quantity=serializer.validated_data['quantity'])
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartRemoveView(APIView):

    def delete(self, request, product_id):
        cart = CartApp(self.request.user)
        cart.remove(product_id=product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
