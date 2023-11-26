from rest_framework import serializers
from product.models import Product, Manufacturer, Category, Image


class CategoryVersionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug'
        ]


class ManufacturerVersionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'id',
            'name',
        ]


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'image',
        ]


class ProductSerializers(serializers.ModelSerializer):
    category = CategoryVersionSerializers()
    manufacturer = ManufacturerVersionSerializers()
    image = ImageSerializers(many=True)
    detail_url = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'code',
            'description',
            'detail',
            'price',
            'in_sale',
            'final_price',
            'image',
            'category',
            'manufacturer',
            'detail_url',
            'average_rating'

        ]

    def get_average_rating(self, obj):
        return obj.average_rating()

    def get_detail_url(self, obj):
        return obj.get_absolute_url()
