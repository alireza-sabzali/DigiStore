from rest_framework import serializers
from product.models import Product, Color, Comments, Images


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('image',)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comments
        fields = ('user', 'text', 'created')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    images      = ImageSerializer(many=True, read_only=True)
    comments    = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'images', 'description', 'created', 'updated', 'status',
                  'price', 'discount', 'final_price', 'product_number', 'available', 'comments')
