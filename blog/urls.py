from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]
