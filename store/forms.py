from django.forms import ModelForm
from store.models import Product, Image


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'amount', 'category']


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
