# -*- coding: utf-8 -*-

from django.db import models
# Create your models here.

class Tomcat(models.Model):
    memory = models.IntegerField(verbose_name="已使用内存")
    time = models.DateTimeField(verbose_name="记录时间")

    def __unicode__(self):
        # return str(self.time) + "-" + str(self.memory) + 'MB'
        return str(self.memory)


