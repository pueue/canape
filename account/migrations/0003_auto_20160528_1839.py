# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
