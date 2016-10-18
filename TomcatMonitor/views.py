from django.shortcuts import render
from django.http import HttpResponse
from models import *
from utils import TomcatMonitorClass

import json
# Create your views here.
def test(request):
    return render(request,'tomcatMonitor\\tomcatMonitor.html')

def test1(request):
    return HttpResponse(json.dumps({'redcode':0,'msg':"HelloWorld"}))

#For tomcat memory

def TomcatMemory(request):
    memory = Tomcat.objects.all().order_by('-id')[0:60]  #get the lastest 15 records
    data_x = []
    data_value = []
    for m in memory:
        data_x.insert(0,m.time.strftime('%H:%M'))
        data_value.insert(0,int(m.memory))
    return render(request,'tomcatMonitor\\tomcatMonitor.html',locals())

def getTomcatMemory(request):
    memory = Tomcat.objects.all().order_by('-id')[0:60]  # get the lastest 15 records
    data_x = []
    data_value = []
    for m in memory:
        data_x.insert(0, m.time.strftime('%H:%M'))
        data_value.insert(0, int(m.memory))
    return HttpResponse(json.dumps({'data_x':data_x,'data_value':data_value}))
#For tomcat Threads

def TomcatThreads(request):
    pass