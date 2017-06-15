# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academic_plan',
            options={'verbose_name': 'Academic_plan'},
        ),
        migrations.AlterModelOptions(
            name='academic_step',
            options={'verbose_name': 'Academic degree'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'Organization'},
        ),
        migrations.AlterModelOptions(
            name='salary',
            options={'verbose_name': 'Salary'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name': 'Speciality'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Subject'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher'},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'verbose_name': 'Training dates'},
        ),
    ]