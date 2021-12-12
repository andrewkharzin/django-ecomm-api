from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_id', 'title', 'author', 'slug', 'price', 'in_stock',
        'created', 'updated'
    ]
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title', )}
