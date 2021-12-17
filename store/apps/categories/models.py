from uuid import uuid4

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    category_id = models.CharField(max_length=16,
                                   default=uuid4,
                                   primary_key=True,
                                   editable=False)
    name = models.CharField(_("Category name"), max_length=255, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    icon = models.ImageField(upload_to='images/category/icns/%Y/%m/%d',
                             blank=True)
    image = models.ImageField(upload_to='images/category/img/%Y/%m/%d',
                              blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name
