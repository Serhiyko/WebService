# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-14 22:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_alrogithm_algorithm_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alrogithm',
            old_name='algorithm_value',
            new_name='algorithm_variable',
        ),
    ]
