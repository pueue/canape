# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postage', '0003_code_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postage',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
    ]