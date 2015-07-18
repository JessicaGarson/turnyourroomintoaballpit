# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Length',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('length_of_room', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Width',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width_of_room', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
