# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-16 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_remove_courseorg_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', max_length=200, upload_to='teacher/%Y/%m', verbose_name='教师图片'),
        ),
    ]
