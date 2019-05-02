from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.views import LoginView

@login_required(login_url='/admin') 
def dash(request):
     return render(request, 'dashboard/index.html')