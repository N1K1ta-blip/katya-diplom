from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ADMIN = 'ADM'
    CLIENT = 'CLI'
    USER_PERMISSION_CHOICES = [
        (ADMIN, 'Админ'),
        (CLIENT, 'Пользователь'),
    ]
    perm = models.CharField(
        max_length=3,
        choices=USER_PERMISSION_CHOICES,
        default=CLIENT
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField(max_length=12, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()