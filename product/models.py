from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

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

    @property
    def get_version(self):
        for version in self.product_version.all():
            return version.pk

    def save(self, *args, **kwargs):
        if self.in_sale:
            self.final_price = self.price - \
                (self.price * self.sale_percent / 100)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"pk": self.get_version})

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
