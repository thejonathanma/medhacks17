# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from healthprovider.models import Provider

# Create your views here.

def profile(request):
    user = request.user
    provider = Provider.objects.get(user_id=user.id)

    context = {
        'profile': provider,
        'user': user
    }
    return render(request, "user/profile.html", context)
