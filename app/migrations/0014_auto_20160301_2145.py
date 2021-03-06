# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20160223_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryrequest',
            name='action_needed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deliveryrequest',
            name='calltime_notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='deliveryrequest',
            name='left_message',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deliveryrequest',
            name='no_contact',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='deliveryrequest',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
