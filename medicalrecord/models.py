# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from index.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Genmedrecords(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    physician_name = models.CharField(max_length=200, default="")
    physician_num = models.IntegerField(default=None, null=True)
    physician_address = models.CharField(max_length=200, default="")
    vacc_date = models.DateField(default=None, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Prescription(models.Model):
    genmedrecords = models.ForeignKey(Genmedrecords, on_delete=models.CASCADE)
    past_meds = models.CharField(max_length=200, default="")
    current_meds = models.CharField(max_length=200, default="")
    surgery = models.CharField(max_length=200, default="")
    vaccinations = models.CharField(max_length=200, default="")
