from django.urls import path
from .views import WishlistAPIView, BasketAPIView

urlpatterns = [
    path('api/wishlist/', WishlistAPIView.as_view(), name='api_wishlist'),
    path('api/basket/', BasketAPIView.as_view(), name='api_basket'),
]
