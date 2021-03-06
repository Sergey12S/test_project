# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, verbose_name='username')),
                ('first_name', models.CharField(max_length=150, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last_name')),
                ('avatar', models.ImageField(upload_to='users_image', verbose_name='avatar')),
                ('birth_date', models.DateField(null=True, verbose_name='birth_date')),
                ('rating', models.IntegerField(default=0, verbose_name='rating')),
            ],
        ),
    ]
