# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import  User
# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=225)
    date = models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User)
