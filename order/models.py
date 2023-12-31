from django.db import models
from product.models import Product
from account.models import User

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_wishlist")
    products = models.ManyToManyField(Product, related_name="wishlist_products")

    def __str__(self):
        return f"{self.user}'s wishlist"

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"


class BasketItem(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name="basket_product")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_basket_item")

    def __str__(self):
        return f"{self.user.full_name}'s basket item"

    def get_subtotal(self):
        if self.product.in_sale:
            return round(self.product.final_price*self.quantity, 2)
        return round(self.product.price*self.quantity, 2)

    class Meta:
        verbose_name = "Basket Item"
        verbose_name_plural = "Basket Items"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_basket")
    products = models.ManyToManyField(BasketItem, related_name="basket_products")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.full_name}'s basket"
    
    def get_total(self):
        total = 0
        for basket_item in self.products.all():
            total += basket_item.get_subtotal()
        return round(total, 2)

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"

