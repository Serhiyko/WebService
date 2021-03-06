# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-14 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20161224_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alrogithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorithm_name', models.CharField(max_length=100)),
                ('algorithm_text', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'algorithm',
                'verbose_name_plural': 'Алгоритм',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'customer',
                'verbose_name_plural': 'Користувачі',
            },
        ),
        migrations.AlterModelOptions(
            name='academic_plan',
            options={'ordering': ['academic_teach'], 'verbose_name_plural': 'Академічний план'},
        ),
        migrations.AlterModelOptions(
            name='academic_step',
            options={'ordering': ['academic_step_name'], 'verbose_name_plural': 'Наукова степінь'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['organization_name'], 'verbose_name_plural': 'Організації'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'ordering': ['speciality_name'], 'verbose_name_plural': 'Спеціальності'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['student_lname'], 'verbose_name_plural': 'Студенти'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['subject_name'], 'verbose_name_plural': 'Предмети'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['teacher_lname', 'teacher_fname'], 'verbose_name_plural': 'Викладачі'},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ['training_spec'], 'verbose_name_plural': 'Терміни навчання'},
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_spec',
        ),
        migrations.AddField(
            model_name='alrogithm',
            name='algorithm_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Customer'),
        ),
    ]
