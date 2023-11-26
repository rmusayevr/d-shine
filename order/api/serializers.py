from rest_framework import serializers
from order.models import Wishlist, BasketItem, Basket
from product.api.serializers import ProductSerializers


class WishlistSerializer(serializers.ModelSerializer):
    products = ProductSerializers(many=True)

    class Meta:
        model = Wishlist
        fields = [
            'user',
            'products'
        ]

class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductSerializers()
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = BasketItem
        fields = [
            'user',
            'product',
            'quantity',
            'subtotal',
        ]

    def get_subtotal(self, obj):
        return obj.get_subtotal()
    

class BasketSerializer(serializers.ModelSerializer):
    products = BasketItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = [
            'user',
            'products',
            'total'
        ]

    def get_total(self, obj):
        return obj.get_total()

