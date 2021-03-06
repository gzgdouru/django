# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-14 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_courseorg_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.PositiveIntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students',
            field=models.PositiveIntegerField(default=0, verbose_name='学习人数'),
        ),
    ]
