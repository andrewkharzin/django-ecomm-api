from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from store.apps.categories.models import Category
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager,
                     self).get_queryset().filter(is_active=True)


class Product(models.Model):
    product_id = models.CharField(max_length=16,
                                  default=uuid4,
                                  primary_key=True,
                                  editable=False)
    category = models.ForeignKey(Category,
                                 related_name='product',
                                 on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='product_creator')
    title = models.CharField(_("Product title"), max_length=255)
    author = models.CharField(_("Author"), max_length=50, default='admin')
    description = models.TextField(_("Description"), blank=True)
    image = models.ImageField(upload_to='images/products/imgs/%Y/%m/%d')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(_("Price"), max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(_("In Stock"), default=True)
    is_active = models.BooleanField(_("Is Active"), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        managed = True
        verbose_name_plural = 'Products'
        ordering = ('-created', )

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title