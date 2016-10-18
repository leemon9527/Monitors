# -*- coding: utf-8 -*-
__author__ = 'leemon'
import sys
import jpype
from jpype import java
from jpype import javax
import time

reload(sys)
sys.setdefaultencoding('utf-8')

class TomcatMonitorClass:

    def __init__(self,host,port,username='',password=''):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def get_java_vm_connection(self):
        '''
        getMBeanServerConnection
        :return:
        '''
        URL = "service:jmx:rmi:///jndi/rmi://%s:%d/jmxrmi" % (self.host, self.port)
        # this it the path of your libjvm /usr/lib/jvm/sun-jdk-1.6/jre/lib/amd64/server/libjvm.so on linux

        #windows的jvm路径，修改为你自己的
        jpype.startJVM("C:\\Program Files (x86)\\Java\\jre1.6.0\\bin\\client\\jvm.dll")
        java.lang.System.out.println("JVM load OK")

        jhash = java.util.HashMap()
        jarray = jpype.JArray(java.lang.String)([self.username, self.password])
        jhash.put(javax.management.remote.JMXConnector.CREDENTIALS, jarray);
        jmxurl = javax.management.remote.JMXServiceURL(URL)
        jmxsoc = javax.management.remote.JMXConnectorFactory.connect(jmxurl, jhash)
        connection = jmxsoc.getMBeanServerConnection();

        return connection

    def memory(self):
        '''
        获取当前内存使用量
        :return:
        '''
        if not self.connection:
            self.connection = self.get_java_vm_connection()
        # Memory is a special case the answer is a Treemap in a CompositeDataSupport
        object = "java.lang:type=Memory"
        attribute = "HeapMemoryUsage"
        attr = self.connection.getAttribute(javax.management.ObjectName(object), attribute)

        return {attribute: str(attr.contents.get("used").value/1024/1024) + 'M'}

    def memoryMB(self):
        '''
        获取当前内存使用量
        :return:
        '''
        if not self.connection:
            self.connection = self.get_java_vm_connection()
        # Memory is a special case the answer is a Treemap in a CompositeDataSupport
        object = "java.lang:type=Memory"
        attribute = "HeapMemoryUsage"
        attr = self.connection.getAttribute(javax.management.ObjectName(object), attribute)

        return {attribute: str(attr.contents.get("used").value/1024/1024) }

    def threads(self):
        if not self.connection:
            self.connection = self.get_java_vm_connection()
        object = "java.lang:type=Threading"
        attribute = "ThreadCount"
        attr = self.connection.getAttribute(javax.management.ObjectName(object), attribute)
        return {attribute:attr.value}

    def threadPool(self):
        if not self.connection:
            self.connection = self.get_java_vm_connection()
        object = 'Catalina:type=ThreadPool,*'
        attribute = {0: 'maxThreads', 1: 'currentThreadCount', 2: 'currentThreadsBusy'}
        threads = self.connection.queryNames(javax.management.ObjectName(object),None)
        threadPool={}
        i=0
        for thread in threads:
            port_name = thread.getKeyProperty('name')
            objname = thread.getCanonicalName()
            maxThreads = self.connection.getAttribute(javax.management.ObjectName(objname),attribute[0]).value
            currentThreadCount = self.connection.getAttribute(javax.management.ObjectName(objname),attribute[1]).value
            currentThreadsBusy = self.connection.getAttribute(javax.management.ObjectName(objname),attribute[2]).value
            pool={'portName':port_name,'maxThreads':maxThreads,'currentThreadCount':currentThreadCount,'currentThreadsBusy':currentThreadsBusy}
            threadPool[i]=pool
            i+=1
        return threadPool
    def info(self):
        if not self.connection:
            self.connection = self.get_java_vm_connection()
        object = 'java.lang:type=Runtime'
        attribute = {0:'VmVendor',1:'VmName',2:'VmVersion',3:'StartTime'}
        #软件厂商
        VmVendor = self.connection.getAttribute(javax.management.ObjectName(object), attribute[0])
        #软件程序
        VmName = self.connection.getAttribute(javax.management.ObjectName(object), attribute[1])
        #软件版本
        VmVersion = self.connection.getAttribute(javax.management.ObjectName(object), attribute[2])
        #启动时间
        start_timestamp = self.connection.getAttribute(javax.management.ObjectName(object),attribute[3]).value/1000
        ltime =  time.localtime(start_timestamp)
        StartTime = time.strftime("%Y-%m-%d %H:%M:%S",ltime)
        now_timestamp = time.time()
        Uptime_seconds = now_timestamp - start_timestamp
        Uptime = format_uptime(Uptime_seconds)
        return {'VmVendor':VmVendor,'VmName':VmName,'VmVersion':VmVersion,'StartTime':StartTime,'Uptime':Uptime}

    def session(self):
        if not self.connection:
            self.connection = self.get_java_vm_connection()
        object = 'Catalina:type=Manager,*'
        attribute = {0: 'maxActiveSessions', 1: 'activeSessions', 2: 'sessionCounter'}
        names =  self.connection.queryNames(javax.management.ObjectName(object),None)
        app_session={}
        i=0
        for name in names:
            objname =  name.getCanonicalName()
            appname = name.getKeyProperty('context').lstrip('/')
            if not appname:
                continue
            maxActiveSessions = self.connection.getAttribute(javax.management.ObjectName(objname),attribute[0]).value
            activeSessions = self.connection.getAttribute(javax.management.ObjectName(objname),attribute[1]).value
            sessionCounter = self.connection.getAttribute(javax.management.ObjectName(objname),attribute[2]).value
            app = {'appname':appname,'maxActiveSessions':maxActiveSessions,'activeSessions':activeSessions,'sessionCounter':sessionCounter}
            app_session[i]=app
            i+=1
        return app_session
def format_uptime(uptime):
    format_uptime = '%s %s,%s %s,%s %s'
    DAY=60*60*24
    HOUR=60*60
    MINUTE=60
    day = int(uptime/DAY)
    hour = int(uptime%DAY/HOUR)
    minute = int(uptime%DAY%HOUR/MINUTE)
    d_str = 'days' if day >1 else 'day'
    h_str = 'hours' if hour>1 else 'hour'
    m_str = 'mins' if min>1 else 'min'
    return format_uptime % (day,d_str,hour,h_str,minute,m_str)


def main():
    pass

if __name__ == '__main__':
    main()