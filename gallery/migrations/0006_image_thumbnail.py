# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_remove_image_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.FileField(default='nothing', upload_to=b'thumbs/%Y%m%d'),
            preserve_default=False,
        ),
    ]
