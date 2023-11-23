from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories/')
    slug = models.SlugField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products/')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'{self.id}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    code = models.CharField(max_length=100)
    description = models.TextField()
    detail = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_sale = models.BooleanField(default=False)
    sale_percent = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='product_category')
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name='product_manufacturer')
    image = models.ManyToManyField(Image, related_name='product_image')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        if self.in_sale:
            self.final_price = self.price - \
                (self.price * self.sale_percent / 100)
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def average_rating(self):
        reviews = self.product_review.all()
        total_ratings = sum(review.rating for review in reviews)
        num_reviews = len(reviews)

        if num_reviews > 0:
            return round(total_ratings / num_reviews)
        else:
            return 0  

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.slug})


class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_review')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.name
