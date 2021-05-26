# Generated by Django 3.1.4 on 2021-05-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_profile_perm'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='perm',
            field=models.CharField(choices=[('ADM', 'Админ'), ('CLI', 'Пользователь')], default='CLI', max_length=3),
        ),
    ]