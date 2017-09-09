# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from index.models import UserForm
from patient.models import PatientForm, Patient
from healthprovider.models import ProviderForm, Provider

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
            print (form.errors)
    else:
        return render(request, "index/create_account.html", {'form': UserForm})

def create_patient_profile(request):
    patient = Patient.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('/patient/profile/')
        else:
            print (form.errors)
    else:
        form = PatientForm(instance=patient)
        return render(request, "index/create_profile.html", {'form': form})

def create_provider_profile(request):
    provider = Provider.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        form = ProviderForm(request.POST, instance=provider)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.save()
            return redirect('/')
        else:
            print form.errors
    else:
        form = ProviderForm(instance=provider)
        return render(request, "index/create_profile.html", {'form': form})
