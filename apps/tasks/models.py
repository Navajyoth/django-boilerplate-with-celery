from django.db import models
from django.utils import timezone

# Create your models here.
from apps.clients.models import Client
from apps.exercises.models import Exercise


class Task(models.Model):

    client = models.ForeignKey(Client, related_name='tasks')
    date = models.DateField(default=timezone.now)
    count = models.PositiveSmallIntegerField(default=0)
    comment = models.CharField(max_length=256)
    exercise = models.ForeignKey(Exercise, related_name='tasks')

    def __str__(self):
        return self.client.name + '-' + self.exercise.name + ' - ' + str(self.date)
