# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=200, default=None)
    phone_number = models.IntegerField(default=None)
    profile_picture = models.FileField(upload_to='member_images/', blank=True)
    insurance = models.CharField(max_length=1000, default=None)
    dob = models.DateField(default=None)

    def __str__(self):
        return self.first_name + " " + self.last_name

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        # exclude = ['user']

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.patient.save()
