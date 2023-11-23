from django.urls import path
from .views import CategoryListView, product, product_detail

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/', product, name='products'),
    path('product_detail/', product_detail, name='product_detail'),
]
