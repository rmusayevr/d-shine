from django.shortcuts import render
from .forms import ContactForm
from .models import Team

def home(request):
    return render(request, 'index.html')


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
