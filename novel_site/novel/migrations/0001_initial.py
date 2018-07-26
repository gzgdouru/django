# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-26 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbFullTimeMage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_url', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('chapter_name', models.CharField(blank=True, max_length=255, null=True)),
                ('chapter_content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_full_time_mage',
                'ordering': ['-chapter_url'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbNovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('novel_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('site_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('chapter_table', models.CharField(blank=True, max_length=64, null=True, unique=True)),
            ],
            options={
                'db_table': 'tb_novel',
                'managed': False,
            },
        ),
    ]
