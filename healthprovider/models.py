# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, default = "")
    last_name = models.CharField(max_length=200, default = "")
    phone_number = models.CharField(max_length=15, default = "")
    profile_picture = models.FileField(upload_to='member_images/', default=None, null=True)
    dob = models.DateField(default=None, null=True)
    insurance_accepted = ArrayField(models.CharField(max_length=200), default = [])
    number_of_patients = models.IntegerField(default=None, null=True)
    office_address = models.TextField(default = "")
    office_city = models.CharField(max_length=200, default="")
    office_state = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name

class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'
        # exclude = ['user']
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Provider.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.provider.save()
