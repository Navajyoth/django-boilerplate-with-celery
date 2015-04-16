from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework import serializers

from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer
# Create your views here.

# def home(request):
#     return HttpResponse('site under construction')

class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
