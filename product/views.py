from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product, Review

def product(request):
    return render(request, 'product.html')


def product_detail(request):
    return render(request, 'product_detail.html')

class CategoryListView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'
