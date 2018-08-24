# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-17 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20180817_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher_clue',
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='', max_length=100, verbose_name='老师告诉你能学到什么'),
        ),
    ]