# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-30 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170830_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/home/images/', validators=[home.models.file_size]),
        ),
    ]
