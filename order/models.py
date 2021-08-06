from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product


class Order(models.Model):
    user    = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order           = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product         = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_count   = models.PositiveIntegerField()
    product_cost    = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.order.user.username
