# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TomcatMonitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomcat',
            name='time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
