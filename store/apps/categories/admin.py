from django.contrib import admin

from .forms import CategoryForm
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'image',
    ]
    prepopulated_fields = {'slug': ('name', )}
    form = CategoryForm
