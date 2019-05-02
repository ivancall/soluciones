# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

def home(request):
    return render(request,'landing/index.html')

# Create your views here.
