# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-24 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_auto_20180824_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='images',
            new_name='image',
        ),
    ]