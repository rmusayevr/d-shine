from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from order.models import Basket, Wishlist

class CartView(LoginRequiredMixin, TemplateView):
    template_name = "cart.html"
    model = Basket

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        user_basket = Basket.objects.filter(user = self.request.user.id, is_active=True).first()
        total = 0
        if user_basket:
            all_products = user_basket.products.all()
            for product in all_products:
                total += product.get_subtotal()
            context['total'] = user_basket.get_total()
            context['products'] = all_products
        return context

class WishlistView(LoginRequiredMixin, TemplateView):
    template_name = "wishlist.html"
    model = Wishlist

    def get_context_data(self, **kwargs):
        context = super(WishlistView, self).get_context_data(**kwargs)
        user_wishlist = Wishlist.objects.filter(user = self.request.user.id).first()
        if user_wishlist:
            all_products = user_wishlist.products.all()
            context['products'] = all_products
        return context
    

class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = "checkout.html"
    model = Basket

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        user_basket = Basket.objects.filter(user = self.request.user.id, is_active=True).first()
        total = 0
        if user_basket:
            all_products = user_basket.products.all()
            for product in all_products:
                total += product.get_total()
            context['total'] = total
            context['products'] = all_products
        return context
