# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160222_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualhelpoffer',
            name='other_help',
            field=models.TextField(blank=True, null=True),
        ),
    ]
