from django.contrib import admin
from .models import Wishlist, Basket, BasketItem

admin.site.register(Wishlist)
admin.site.register(Basket)
admin.site.register(BasketItem)
