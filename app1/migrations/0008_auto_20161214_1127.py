# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_salary_salary_mouth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_kod',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]