from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    materials = models.CharField(max_length=255, blank=True, null=True)
    country_of_origin = models.CharField(max_length=255, blank=True, null=True)
    fit = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField()
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    has_sizes = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.name
    



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user} on {self.product.name} - {self.rating} Stars"
