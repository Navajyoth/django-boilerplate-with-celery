from django.db import models
from django.conf import settings
from django.utils import timezone

from apps.account.base import UserProfileBase
# from apps.clients.models import Client
# Create your models here.


class Trainer(UserProfileBase):
    photo = models.FileField(upload_to='images/trainers')
    monthly_rate = models.PositiveSmallIntegerField(max_length=4)
    month_rate_3 = models.PositiveSmallIntegerField(max_length=4)
    month_rate_6 = models.PositiveSmallIntegerField(max_length=4)
    month_rate_12 = models.PositiveSmallIntegerField(max_length=4)


# class Task(models.Model):
#     # client = models.ForeignKey(Client, related_name='tasks')
#     date = models.DateField(default=timezone.now)
#     excercise_type = models.CharField(max_length=40)
#     count = models.PositiveSmallIntegerField(default=0)
#     comment = models.CharField(max_length=256)
#     media = models.ForeignKey(Media, related_name='tasks')


# class Routine(Task):
#     pass

#     # class Meta:
#     #     fields = (
#     #         'client', 'date', 'excercise_type', 'count', 'comment', 'media'
#     #     )

# class Media(models.Model):
#     video = models.FileField(upload_to='videos')
#     image = models.FileField(upload_to='images')