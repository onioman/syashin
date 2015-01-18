# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150102_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imgfile',
            field=models.FileField(default='nothing', upload_to=b'upload/%Y%m%d'),
            preserve_default=False,
        ),
    ]
