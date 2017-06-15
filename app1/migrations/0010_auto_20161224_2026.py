# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20161215_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic_step',
            name='academic_step_kod',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organization',
            name='organization_kod',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='speciality_kod',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_kod',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_kod_pred',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_kod',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]