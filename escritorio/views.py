# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.views import LoginView

@login_required(login_url='/admin') 
def esc(request):
     return render(request, 'escritorio/base.html')

#@login_required(login_url='/admin') 
#def esc(request):
#     return redirect('/')
    


