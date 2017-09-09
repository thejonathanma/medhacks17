# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from patient.models import Patient

# Create your views here.

def profile(request):
    user = request.user
    patient = Patient.objects.get(user_id=user.id)

    context = {
        'patient': patient,
        'user': user
    }

    return render(request, "user/profile.html", context)
