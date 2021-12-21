from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .forms import CategoryForm
from .models import Category

admin.site.register(Category, MPTTModelAdmin)
