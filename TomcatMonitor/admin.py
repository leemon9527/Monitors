from django.contrib import admin
from models import *
# Register your models here.

# admin.site.register(Tomcat)

class TomcatAdmin(admin.ModelAdmin):
    list_display = ('time','memory')

admin.site.register(Tomcat,TomcatAdmin)