# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(verbose_name=b'date added')),
                ('taken_date', models.DateTimeField(verbose_name=b'date taken')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
