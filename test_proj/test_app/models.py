from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_image', verbose_name='Avatar')
    birth_date = models.DateField(null=True, verbose_name='birth_date')
