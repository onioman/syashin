from django.db import models

# Create your models here.
class Image(models.Model):
    location = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added')
    taken_date = models.DateTimeField('date taken')

    def __str__(self):
        return "Image: %s taken %s"%(self.location, self.taken_date)
