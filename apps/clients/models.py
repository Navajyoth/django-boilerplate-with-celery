from django.db import models
from appps.account.base import UserProfileBase
from apps.trainers.models import Trainer


class Client(UserProfileBase):
    trainer = models.ForeignKey(Trainer, related_name='clients')
    height = models.CharField(max_length=7)
    weight = models.CharField(max_length=7)
    bloodtype = models.CharField(max_length=5)
    occupation = models.CharField(max_length=30)
    goal_weight = models.CharField(max_length=7)
    goal_achieved = models.BooleanField(default=False)
    wake_up_time = models.DateTimeField(default=timezone.now)
    bed_time = models.DateTimeField(default=timezone.now)
    sit_more_than_30hrs_per_week = models.BooleanField(default=False)
    constant_back_pain = models.BooleanField(default=False)
    currently_pregnant = models.BooleanField(default=False)
    weekly_workout_schedule = models.CharField(max_length=25)


class MedicalHistory(models.Model):
    client = models.ForeignKey(Client, related_name='medical histories')
    time_of_injury = models.DateTimeField(
        default=timezone.now, verbose='Hospital Injury'
    )
    comments = models.CharField(max_length=512)


class ClientFeed(models.Model):
    message = models.CharField(max_length=512)
    datetime = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(Client, related_name='Client Feed')
