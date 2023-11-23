from django.shortcuts import render


def product(request):
    return render(request, 'product.html')


def product_detail(request):
    return render(request, 'product_detail.html')


def catalog(request):
    return render(request, 'catalog.html')
