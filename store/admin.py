from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from store.models import Product, Image, Category

class ImageInlineAdmin(admin.StackedInline):
    model = Image
    verbose_name = Image._meta.verbose_name
    verbose_name_plural = Image._meta.verbose_name_plural

@admin.register(Product)
class ProductAdmin(GuardedModelAdmin):
    inlines = [ImageInlineAdmin]

@admin.register(Category)
class CategoryAdmin(GuardedModelAdmin):
    pass