# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20160113_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='username',
            name='email',
            field=models.EmailField(default='default@deuser.app', max_length=254),
        ),
        migrations.AddField(
            model_name='username',
            name='user_age',
            field=models.IntegerField(default=0),
        ),
    ]
