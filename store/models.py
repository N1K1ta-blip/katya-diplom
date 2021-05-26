from django.db import models
import time

def generate_imageset_upload_to(instance, filename=None):
    return f'images/{instance.id}_{str(int(time.time()))}.png'
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"   

    def __str__(self):                           
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта")
    price = models.PositiveIntegerField(verbose_name="Цена продукта")
    amount = models.PositiveIntegerField(verbose_name="Остаток а наличии")
    selled = models.IntegerField(default=0 ,verbose_name="Продано товаров")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title

    def first_image(self):
        return self.images.first()

    def all_images(self):
        return self.images.all()


class Image(models.Model):
    image = models.ImageField(upload_to=generate_imageset_upload_to)
    product = models.ForeignKey(Product, models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return "{}".format(self.image.url)
