from django.contrib import admin
from .models import Category, Image, Manufacturer, Product, Review

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Review)
