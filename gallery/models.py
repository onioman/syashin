import datetime

from django.db import models
from django.utils import timezone

class Image(models.Model):
    location    = models.CharField(max_length=200)
    add_date    = models.DateTimeField('date added')
    taken_date  = models.DateTimeField('date taken')
    title       = models.CharField(max_length=100)

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.add_date <= now

    def __str__(self):
        return "Image: %s taken %s"%(self.title, self.taken_date)

class Album(models.Model):
    images  = models.ManyToManyField(Image)
    name    = models.CharField(max_length=100) 

    def __str__(self):
        return "Album: %s [%s]"%(self.name, len(self.images))
