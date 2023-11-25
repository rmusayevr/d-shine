from django.shortcuts import render
from .forms import ContactForm
from .models import Team
from product.models import Product, Category
from blog.models import Blog
from django.db.models import Avg

def home(request):
    products = Product.objects.annotate(avg_rating=Avg('product_review__rating')).order_by('-avg_rating')[:4]
    categories = Category.objects.all()
    blogs = Blog.objects.all().order_by('-created_at')[1:6]
    last_blog = Blog.objects.last()
    context = {
        'products': products,
        'categories': categories,
        'blogs': blogs,
        'last_blog': last_blog
    }
    return render(request, 'index.html', context=context)


def about(request):
    team = Team.objects.all()
    context = {
        'members': team
    }
    return render(request, 'about.html', context=context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)


def error(request):
    return render(request, '404.html')
