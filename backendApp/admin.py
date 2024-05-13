from django.contrib import admin
from .models import Category, Products

admin.site.register(Category)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=['name', 'quantity', 'description', 'price', 'image', 'created_at']
    
    
    