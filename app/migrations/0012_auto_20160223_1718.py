# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 22:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_auto_20160223_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryrequest',
            name='other_supplies_needed',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deliveryrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]