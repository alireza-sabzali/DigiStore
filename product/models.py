from decimal import Decimal

from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    STATUS_CHOICES = (("draft", "Draft"), ("publish", "Publish"))

    name            = models.CharField(max_length=120)
    description     = models.TextField()
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    status          = models.CharField(max_length=10, choices=STATUS_CHOICES, default='publish')
    product_number  = models.SmallIntegerField(default=1)
    price           = models.DecimalField(max_digits=10, decimal_places=0)
    discount        = models.SmallIntegerField(default=0)

    @property
    def available(self):
        return True if self.product_number > 0 else False

    @property
    def final_price(self):
        return self.price - (self.price * Decimal(self.discount / 100))

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.name


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image   = models.ImageField(upload_to='images')

    def __str__(self):
        return self.product.name


class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user    = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.product.name + self.text[:10]


class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
