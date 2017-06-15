# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20161214_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academic_plan',
            options={'verbose_name_plural': 'Академічний план'},
        ),
        migrations.AlterModelOptions(
            name='academic_step',
            options={'verbose_name_plural': 'Наукова степінь'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name_plural': 'Організації'},
        ),
        migrations.AlterModelOptions(
            name='salary',
            options={'verbose_name_plural': 'Заробітна плата'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name_plural': 'Спеціальності'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Студенти'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name_plural': 'Предмети'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': 'Викладачі'},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'verbose_name_plural': 'Терміни навчання'},
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_kod_pred',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
