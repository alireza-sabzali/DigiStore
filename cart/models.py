from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from django.db.models.signals import post_save


class Cart(models.Model):
    user    = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='carts')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart            = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product         = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity        = models.SmallIntegerField()
    product_cost    = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.cart.user.username


def save_cart_user(sender, **kwargs):
    if kwargs['created']:
        cart_user = Cart(user=kwargs['instance'])
        cart_user.save()


post_save.connect(save_cart_user, sender=get_user_model())
