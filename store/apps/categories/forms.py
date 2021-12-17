from django import forms
from django_svg_image_form_field import SvgAndImageFormField
from store.apps.categories.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []
        field_classes = {
            'icon': SvgAndImageFormField,
        }
