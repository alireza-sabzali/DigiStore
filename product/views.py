from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from product.models import Product, Color, Comments, Images
from .permissions import IsAdminOrReadOnly, IsAdmin
from .serializers import ProductSerializer, CommentSerializer, \
    ImageSerializer, ColorSerializer
from rest_framework.views import APIView


# ============= Product Views =====================
class ProductListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# ============= Comment Views =====================
class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product, user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


# ============= Color Views =====================
class ColorCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Color.objects.all()
    serializer_class = ColorSerializer


# ============= Image Views =====================
class ImageCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Images.objects.all()
    serializer_class = ImageSerializer

