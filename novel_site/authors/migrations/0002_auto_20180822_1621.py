# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-22 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.TextField(default='', verbose_name='详细介绍'),
        ),
        migrations.AlterField(
            model_name='author',
            name='desc',
            field=models.CharField(default='', max_length=255, verbose_name='简介'),
        ),
    ]
