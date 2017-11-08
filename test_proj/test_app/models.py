from django.db import models


class Client(models.Model):
    username = models.CharField(max_length=150, verbose_name="Логин")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    avatar = models.ImageField(upload_to="users_image", verbose_name="Аватар")
    birth_date = models.DateField(verbose_name="Дата рождения")
    rating = models.PositiveSmallIntegerField(default=0,
                                              verbose_name="Рейтинг")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.username
