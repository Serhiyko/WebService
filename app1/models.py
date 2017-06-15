# -*- coding: utf-8 -*-
from django.db import models


class Alrogithm(models.Model):
    class Meta:
        db_table = 'algorithm'
        verbose_name_plural = 'Алгоритм'

    algorithm_name = models.CharField(max_length=100)
    algorithm_text = models.CharField(max_length=1000)
    algorithm_variable = models.CharField(max_length=200, default='')
    algorithm_creater = models.CharField(max_length=30)


class Customer(models.Model):
    class Meta:
        db_table = 'customer'
        verbose_name_plural = "Користувачі"

    customer_name = models.CharField(max_length=30)
    customer_id_algor = models.ForeignKey(Alrogithm, on_delete=models.CASCADE)

