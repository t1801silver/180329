# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 18:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20180321_0322'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='planpost',
            table='plan_posts',
        ),
    ]
