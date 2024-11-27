from django.db import models
from apps.user.models import Consumer
from apps.product.models import Product


class WishList(models.Model):
    consumer = models.OneToOneField(Consumer, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField("product.Product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Wishlist for {self.consumer.user.username}"


class WishListProduct(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity}) in wishlist"
