# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date

# Create your models here.
class HealthRecord(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField(default=None)
    insurance = models.CharField(max_length=1000, default=None)
    current_medication = ArrayField(models.CharField(max_length=200))
