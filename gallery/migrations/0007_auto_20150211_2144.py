# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from django.db import models, migrations
from django.core.files import File

from gallery.models import Image

def create_thumbnails(apps, schema_editor):
    Image = apps.get_model('gallery', 'Image')
    index = 0
    for image in Image.objects.all():
        from PIL import Image as PILImage
        width = 160
        img = PILImage.open(image.imgfile)
        height = int(img.size[0] / img.size[1] * width)
        img.thumbnail((width, height), PILImage.ANTIALIAS)
        img.save('/tmp/photo.thumbnail', 'JPEG')
        f = open('/tmp/photo.thumbnail')
        image.thumbnail.save('image_%s.thumbnail'%index, File(f))
        index = index + 1

class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_image_thumbnail'),
    ]

    operations = [
        migrations.RunPython(create_thumbnails),
    ]
