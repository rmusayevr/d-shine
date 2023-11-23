from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Product, Review
from .forms import ReviewForm
from django.shortcuts import redirect

class ProductListView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    ordering = ['-created_at']

    def get_queryset(self):
        category = self.request.GET.get("category")
        if category:
            self.queryset = Product.objects.filter(
                category__slug=category).all()
        else:
            self.queryset = Product.objects.all()
        return self.queryset


class ProductDetailView(CreateView, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    form_class = ReviewForm

    def get_object(self):
        return Product.objects.get(slug=self.kwargs.get("slug"))
    
    def form_valid(self, form):
        form.instance.product = self.get_object()
        form.instance.save()
        return redirect(self.get_object().get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context['related_products'] = Product.objects.filter(
            category=self.get_object().category).exclude(slug=self.get_object().slug)[:4]
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'
