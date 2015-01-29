import datetime

from django.db import models
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)

class Image(models.Model):
    imgfile     = models.FileField(upload_to='upload/%Y%m%d')
    add_date    = models.DateTimeField('date added')
    taken_date  = models.DateTimeField('date taken')
    title       = models.CharField(max_length=100)

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.add_date <= now

    @staticmethod
    def create(imgfile, title):
        now = timezone.now()

        #image data
        from PIL import Image as PILImage
        import ExifTags
        img = PILImage.open(imgfile)
        exif_data = img._getexif()
        exif = {
            ExifTags.TAGS[k] : v
            for k, v in exif_data.items()
            if k in ExifTags.TAGS
        }
        logger.info(exif)
        taken_date = datetime.datetime.strptime(exif['DateTimeOriginal'], "%Y:%m:%d %H:%M:%S")
        new_image = Image(imgfile = imgfile, title = title,
                add_date = now, taken_date = taken_date)
        return new_image

    def __str__(self):
        return "Image: %s taken %s"%(self.title, self.taken_date)

class Album(models.Model):
    images  = models.ManyToManyField(Image)
    name    = models.CharField(max_length=100) 

    def size(self):
        return len(self.images.all())

    def __str__(self):
        return "Album: %s [%s]"%(self.name, len(self.images.all()))
