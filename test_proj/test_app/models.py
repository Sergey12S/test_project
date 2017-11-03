from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    avatar = models.ImageField(upload_to='users_image', verbose_name='Avatar')
    birth_date = models.DateField(null=True, verbose_name='birth_date')
    rating = models.IntegerField(default=0, verbose_name='rating')
    likes = models.ManyToManyField('test_app.Like', related_name='likes', blank=True)


class Like(models.Model):

    title = models.CharField(verbose_name='title', max_length=10, default='like', blank=True)
    image = models.ForeignKey(User, related_name='image_like')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created date')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'
