from rest_framework.generics import ListAPIView
from product.models import Product
from .serializers import ProductSerializers

class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

