# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160604_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
