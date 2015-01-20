# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.files import File

from gallery.models import Image
import os

def from_location_to_imgfile(apps, schema_editor):
    Image = apps.get_model('gallery', 'Image')
    index = 0
    for image in Image.objects.all():
        f = open("gallery/static/gallery/assets/%s"%image.location)
        image.imgfile.save('image_%s'%index, File(f))
        index = index + 1

class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image_imgfile'),
    ]

    operations = [
        migrations.RunPython(from_location_to_imgfile),
    ]
