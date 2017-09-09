# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from index.models import UserForm
from patient.models import PatientForm, Patient

from django.contrib.auth import authenticate, login

def index(request):
    return render(request, "index/index.html")

def create_account(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('/create_patient_profile/')
        else:
            print form.errors
    else:
        return render(request, "index/create_account.html", {'form': UserForm})

def upload_file(f):
    with f.upload_to as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def create_patient_profile(request):
    patient = Patient.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            patient = form.save()
            return redirect('/patient/profile/')
        else:
            print form.errors
    else:
        form = PatientForm(instance=patient)
        return render(request, "index/create_profile.html", {'form': form})
