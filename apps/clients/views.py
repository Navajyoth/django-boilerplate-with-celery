from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from apps.clients.models import Client, Feed

def home(request):
    return HttpResponse('site under construction')
