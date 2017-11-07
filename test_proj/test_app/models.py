from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150, verbose_name='username')
    first_name = models.CharField(max_length=150, verbose_name='first_name')
    last_name = models.CharField(max_length=150, verbose_name='last_name')
    avatar = models.ImageField(upload_to='users_image', verbose_name='avatar')
    birth_date = models.DateField(null=True, verbose_name='birth_date')
    rating = models.IntegerField(default=0, verbose_name='rating')
