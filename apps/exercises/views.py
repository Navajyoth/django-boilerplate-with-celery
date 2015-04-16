from django.shortcuts import render

from rest_framework import serializers
from rest_framework import generics

from apps.exercises.models import Exercise
from apps.exercises.serializers import ExerciseSerializer
# Create your views here.

class ExerciseView(generics.ListCreateAPIView):

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
