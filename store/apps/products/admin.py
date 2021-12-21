import modelclone
from django.contrib import admin
from modelclone import ClonableModelAdmin

from .models import *


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(modelclone.ClonableModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]
