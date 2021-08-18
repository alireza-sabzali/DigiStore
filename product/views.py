from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product, Color, Comments, Images
from .permissions import IsAdminOrReadOnly
from .serializers import ProductSerializer, CommentSerializer, \
    ImageSerializer, ColorSerializer


class ProductListView(generics.ListCreateAPIView):
    """
        List all code product, or create a new product
    """
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = ProductSerializer

    def get_queryset(self):
        if 'product' in cache:
            products = cache.get('product')
            return products
        else:
            products = Product.objects.all()
            cache.set('product', products, timeout=300)
            return products


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update or delete a code product.
    """
    permission_classes = [IsAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CommentCreateView(APIView):
    """
        create a new comment
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product, user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteView(generics.DestroyAPIView):
    """
        delete a comment
    """
    permission_classes = [IsAuthenticated]

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class ColorCreateView(APIView):
    """
        create a new color
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorDeleteView(generics.DestroyAPIView):
    """
        delete a color
    """
    permission_classes = [IsAuthenticated]

    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ImageCreateView(APIView):
    """
        create a new image
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDeleteView(generics.DestroyAPIView):
    """
        delete a image
    """
    permission_classes = [IsAuthenticated]

    queryset = Images.objects.all()
    serializer_class = ImageSerializer

