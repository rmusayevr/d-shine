from django.shortcuts import render


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def wishlist(request):
    return render(request, 'wishlist.html')
