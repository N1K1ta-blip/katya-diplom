from django.db import models
import time

def generate_imageset_upload_to(instance, filename=None):
    return f'images/{instance.id}_{str(int(time.time()))}.png'
    


class Work(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return self.title

    def first_image(self):
        return self.images.first()

    def all_images(self):
        return self.images.all()



class Image(models.Model):
    image = models.ImageField(upload_to=generate_imageset_upload_to)
    work = models.ForeignKey(Work, models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return "{}".format(self.image.url)
