# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canape', '0005_auto_20160606_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
