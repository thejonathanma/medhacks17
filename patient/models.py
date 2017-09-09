# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_picture = models.FileField(default=None)
    insurance = models.CharField(max_length=1000, default=None)
    dob = models.DateField(default=None)

    def __str__(self):
        return self.first_name + " " + self.last_name
