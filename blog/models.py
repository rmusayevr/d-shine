from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='authors')
    about = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='blogs')
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_category')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
