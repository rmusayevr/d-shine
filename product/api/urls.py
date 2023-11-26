from django.urls import path
from .views import ProductAPIView
urlpatterns = [
    path('api/products/', ProductAPIView.as_view(), name='api_product_detail')
]
