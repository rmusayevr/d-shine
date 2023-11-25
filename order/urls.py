from django.urls import path
from .views import CartView, WishlistView, CheckoutView


urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
