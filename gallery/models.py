import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    location = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added')
    taken_date = models.DateTimeField('date taken')

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.add_date <= now

    def __str__(self):
        return "Image: %s taken %s"%(self.location, self.taken_date)
