# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_organization_organization_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_spec',
        ),
    ]
