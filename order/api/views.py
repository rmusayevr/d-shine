from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from order.models import Wishlist, Basket, BasketItem
from product.models import Product
from .serializers import WishlistSerializer, BasketSerializer


class WishlistAPIView(APIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        wishlist = Wishlist.objects.filter(user=self.request.user).first()
        serializer = self.serializer_class(wishlist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_pk = request.data.get('product')
        product = Product.objects.filter(pk=product_pk).first()
        if product and self.request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user=self.request.user).first()
            if wishlist:
                wishlist.products.add(product)
            else:
                wishlist = Wishlist.objects.create(user=self.request.user)
                wishlist.products.add(product)
            message = {'success': True,
                       'message': 'Product added to your wishlist.'}
            return Response(message, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        product = request.data.get('product')
        version = Product.objects.filter(pk=product).first()
        if version and self.request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user=self.request.user).first()
            if wishlist:
                wishlist.products.remove(version)
                message = {'success': True,
                           'message': 'Product removed from your wishlist.'}
                return Response(message, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        elif not version and self.request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user=self.request.user).first()
            if wishlist:
                wishlist.products.clear()
                message = {'success': True,
                           'message': 'All products removed from your wishlist.'}
                return Response(message, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class BasketAPIView(APIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get(self, request, *args, **kwargs):
        basket = Basket.objects.filter(user=self.request.user).first()
        serializer = self.serializer_class(basket)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_pk = request.data.get('product')
        quantity = request.data.get('quantity')
        product = Product.objects.filter(pk=product_pk).first()
        if product and self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.request.user).first()
            if basket:
                basket_item = basket.products.filter(product=product).first()
                if basket_item:
                    basket_item.quantity += int(quantity)
                    basket_item.save()
                else:
                    basket_item = basket.products.create(
                        user=self.request.user, product=product, quantity=quantity)
            else:
                basket = Basket.objects.create(user=self.request.user)
                basket_item = basket.products.create(
                    user=self.request.user, products=product, quantity=quantity)
            message = {'success': True,
                       'message': 'Product added to your basket.'}
            return Response(message, status=status.HTTP_201_CREATED)
        
    def patch(self, request, *args, **kwargs):
        ProductDOWN = request.data.get('productDown')
        ProductUP = request.data.get('productUp')
        if ProductDOWN:
            user_basket = BasketItem.objects.get(product=ProductDOWN, user = request.user)
            user_basket.quantity -= 1
            user_basket.save()
            message = {'success': True, 'message' : 'Product has been decreased.'}
            return Response(message, status = status.HTTP_200_OK)
        elif ProductUP:
            user_basket = BasketItem.objects.get(product=ProductUP, user = request.user)
            user_basket.quantity += 1
            user_basket.save()
            message = {'success': True, 'message' : 'Product has been increased.'}
            return Response(message, status = status.HTTP_200_OK)
        

    def delete(self, request, *args, **kwargs):
        product_pk = request.data.get('product')
        product = Product.objects.filter(pk=product_pk).first()
        if product and self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.request.user).first()
            if basket:
                basket_item = basket.products.filter(product=product).first()
                if basket_item:
                    basket_item.delete()
                    message = {'success': True,
                               'message': 'Product removed from your basket.'}
                    return Response(message, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        elif not product and self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.request.user).first()
            if basket:
                basket.products.all().delete()
                message = {'success': True,
                           'message': 'All products removed from your basket.'}
                return Response(message, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
