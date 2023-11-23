from django.urls import path
from .views import home, about, contact, error

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('error/', error, name='error'),
]
