from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from main.models import Work, Image

class ImageInlineAdmin(admin.StackedInline):
    model = Image
    verbose_name = Image._meta.verbose_name
    verbose_name_plural = Image._meta.verbose_name_plural

@admin.register(Work)
class WorkAdmin(GuardedModelAdmin):
    inlines = [ImageInlineAdmin]
