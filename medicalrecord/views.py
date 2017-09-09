# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from index.models import UserForm
# from medicalrecord.models import GenMedRecords, Prescription
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, "medicalrecord/index.html")

# class GenMedRecordsCreate(CreateView):
#     model = GenMedRecords
#     fields = ['name']
#
# class GenMedRecordsUpdate(UpdateView):
#     model = GenMedRecords
#     fields = ['name']
#
# class GenMedRecordsDelete(DeleteView):
#     model = GenMedRecords
#     success_url = reverse_lazy('gen_med_records')
#
# class PrescriptionCreate(CreateView):
#     model = Prescription
#     fields = ['meds']
#
# class PrescriptionUpdate(UpdateView):
#     model = Prescription
#     fields = ['meds']
#
# class PrescriptionDelete(DeleteView):
#     model = Prescription
#     success_url = reverse_lazy('prescription-list')
