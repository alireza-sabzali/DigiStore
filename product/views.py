from django.core.cache import cache
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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


class CommentCreateView(generics.CreateAPIView):
    """
        Create comment for post model.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class ColorDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ImageDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Images.objects.all()
    serializer_class = ImageSerializer
