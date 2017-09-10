# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from patient.models import Patient
from medicalrecord.models import Prescription, Genmedrecords

def index(request):
    return render(request, "medicalrecord/index.html")

def Record(request):
    user = request.user
    patient = Patient.objects.get(user_id=user.id)
    prescription = Prescription.objects.get(genmedrecords_id=genmedrecords.id)
    med_record = Genmedrecords.objects.get(user_id=user.id)

    context = {
        'profile': patient,
        'user': user,
        'prescription': prescription,
        'record': med_record

    }

    return render(request, "medicalrecord/index.html", context)
