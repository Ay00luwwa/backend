from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name