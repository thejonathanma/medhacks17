# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('P', 'Patient'),
        ('H', 'HealthProvider')
    )

    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default='P')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'user_type']
