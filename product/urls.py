from django.urls import path
from .views import catalog, product, product_detail

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('product/', product, name='product'),
    path('product_detail/', product_detail, name='product_detail'),
]
