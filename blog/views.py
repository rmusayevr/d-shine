from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog, Author, Category, Tag, Comment
from .forms import CommentForm
from django.shortcuts import redirect


class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
    paginate_by = 3

    def get_queryset(self):
        category = self.request.GET.get("category")
        author = self.request.GET.get("author")
        tag = self.request.GET.get("tag")
        if category:
            self.queryset = Blog.objects.filter(category__slug=category).all()
        elif author:
            self.queryset = Blog.objects.filter(author__slug=author).all()
        elif tag:
            self.queryset = Blog.objects.filter(tags__slug=tag).all()
        else:
            self.queryset = Blog.objects.all()
        return self.queryset.filter(is_published=True).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Blog.objects.all().order_by('-created_at')[:4]
        context['authors'] = Author.objects.all().order_by('full_name')
        context['categories'] = Category.objects.all().order_by('name')
        context['tags'] = Tag.objects.all().order_by('name')
        return context


class BlogDetailView(CreateView, DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'
    form_class = CommentForm

    def get_object(self):
        return Blog.objects.get(slug=self.kwargs.get("slug"))

    def form_valid(self, form):
        form.instance.blog = self.get_object()
        form.instance.save()
        return redirect('blog_detail', slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Blog.objects.all().order_by('-created_at')[:4]
        context['authors'] = Author.objects.all().order_by('full_name')
        context['categories'] = Category.objects.all().order_by('name')
        context['tags'] = Tag.objects.all().order_by('name')
        context['comments'] = Comment.objects.filter(blog=self.get_object()).order_by('-created_at')
        return context
