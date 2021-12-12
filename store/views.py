from django.shortcuts import render
from store.apps.categories.models import Category
from store.apps.products.models import Product

from django.shortcuts import get_object_or_404, render


def product_all(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {
        'category': category,
        'products': products
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})