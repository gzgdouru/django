# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-20 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180719_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
