# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20150112_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
    ]
