# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    phone_number = models.CharField(max_length=15, default='')
    profile_picture = models.FileField(upload_to='user_profile_images/', blank=True, null=True)
    insurance = models.CharField(max_length=1000, default='')
    dob = models.DateField(default=None, null=True)
    address = models.CharField(max_length=1000, default='')
    city = models.CharField(max_length=500, default='')
    state = models.CharField(max_length=200, default='')
    zip_code = models.CharField(max_length=5, default='')

    def __str__(self):
        return self.first_name + " " + self.last_name

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user']

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.patient.save()
