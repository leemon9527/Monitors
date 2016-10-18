# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TomcatMonitor', '0002_auto_20161017_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomcat',
            name='memory',
            field=models.IntegerField(verbose_name=b'\xe5\xb7\xb2\xe4\xbd\xbf\xe7\x94\xa8\xe5\x86\x85\xe5\xad\x98'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tomcat',
            name='time',
            field=models.DateTimeField(verbose_name=b'\xe8\xae\xb0\xe5\xbd\x95\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
