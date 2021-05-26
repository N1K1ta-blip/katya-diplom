from django.db import models
from django.contrib.auth.models import User
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


class Order(models.Model):
    SELF = 'SEL'
    DELIVERY = 'DEL'
    DELIVERY_TYPE_CHOICES = [
        (SELF, 'Самовывоз'),
        (DELIVERY, 'Доставка'),
    ]

    ONLINE = 'ONL'
    OFFLINE = 'OFL'
    PAYMENT_PLACE_CHOICES = [
        (ONLINE, 'Онлайн'),
        (OFFLINE, 'При получении'),
    ]

    CARD = 'CAR'
    CASH = 'CAS'
    PAYMENT_TYPE_CHOICES = [
        (CARD, 'Картой'),
        (CASH, 'Наличными'),
    ]

    delivery_type = models.CharField(
        max_length=3,
        choices=DELIVERY_TYPE_CHOICES,
        default=SELF
    )
    payment_place = models.CharField(
        max_length=3,
        choices=PAYMENT_PLACE_CHOICES,
        default=ONLINE
    )
    payment_type = models.CharField(
        max_length=3,
        choices=PAYMENT_TYPE_CHOICES,
        default=CARD,
        null=True, blank=True,
    )

    # optional fields
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house = models.CharField(max_length=100, blank=True, null=True)
    corps = models.CharField(max_length=100, blank=True, null=True)
    apartment = models.CharField(max_length=100, blank=True, null=True)

    lease = models.PositiveIntegerField(default=0)


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"   

    def __str__(self):                           
        return str(self.created_at)

    def get_full_address(self):
        result = ""
        if self.city:
            result += f'{self.city}'
        if self.street:
            result += f', {self.street}'
        if self.house:
            result += f', {self.house}'
        if self.corps:
            result += f', {self.corps}'
        if self.apartment:
            result += f', {self.apartment}'
        return result
