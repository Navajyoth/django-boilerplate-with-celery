from django.db import models
from django.conf import settings
from django.utils import timezone

from apps.account.base import UserProfileBase
# from apps.clients.models import Client
# Create your models here.


class Trainer(UserProfileBase):
    photo = models.FileField(upload_to='images/trainers', blank=True)
    monthly_rate = models.PositiveSmallIntegerField(blank=True)
    month_rate_3 = models.PositiveSmallIntegerField(blank=True)
    month_rate_6 = models.PositiveSmallIntegerField(blank=True)
    month_rate_12 = models.PositiveSmallIntegerField(blank=True)
