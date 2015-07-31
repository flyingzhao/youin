#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import paramiko
import time
import MySQLdb
import os
import gobject
from  pyinotify import  WatchManager, Notifier, ProcessEvent, ThreadedNotifier, IN_DELETE, IN_CREATE,IN_MOVED_TO,IN_MOVED_FROM
 



#read ip from local mysql db
pi_id='1'
host='localhost'
user='pi'
passwd='raspberry'
db='piip'
conn=MySQLdb.connect(host=host,user=user,passwd=passwd,db=db)
cur=conn.cursor()
query='select * from iplist where id='+pi_id
cur.execute(query)

data = cur.fetchone()
print data[1]
targetip=data[1]
cur.close()
conn.close()

ISOTIMEFORMAT="%Y-%m-%d %X"


#transmit to target socket
def sendfile(name):
	targetsocket=(targetip,22)
	user="pi"
	pwd="raspberry"
	filename=name.split('/')[-1]
	print filename
	remotepath='/home/pi/youin/download/'+filename
	localpath='/var/www/html/youin/file/'+filename
	print localpath
	print remotepath
	print "初始化链接"+time.strftime( ISOTIMEFORMAT, time.localtime() )
	t = paramiko.Transport(targetsocket)#Create a new SSH session over an existing socket

	t.connect(username = user, password = pwd)#Negotiate an SSH2 session
	print  "建立链接"+time.strftime( ISOTIMEFORMAT, time.localtime() )

	sftp = paramiko.SFTPClient.from_transport(t)#Create an SFTP client channel from an open Transport.
	print  "开始传输"+time.strftime( ISOTIMEFORMAT, time.localtime() )
	sftp.put(localpath,remotepath)#Copy a local file (localpath) to the SFTP server as remotepath.
	print  "传输完成"+time.strftime( ISOTIMEFORMAT, time.localtime() )
	t.close()

	print 'OK'


 #watch the change of dictory
class watchfile(ProcessEvent):
    def process_IN_CREATE(self, event):
        print   "创建文件: %s "  %   os.path.join(event.path, event.name)
        name=os.path.join(event.path, event.name)
        print "Start to transfer"
        sendfile(name)
        print "Transfered successfully"
 
    def process_IN_DELETE(self, event):
        print   "删除文件: %s "  %   os.path.join(event.path, event.name)
 
    def process_IN_MOVED_TO(self, event):
        print   "移来文件: %s "  %   os.path.join(event.path, event.name)
        name=os.path.join(event.path, event.name)
        print "Start to transfer"
        sendfile(name)
        print "Transfered successfully"
 
    def process_IN_MOVED_FROM(self, event):
        print   "移走文件: %s "  %   os.path.join(event.path, event.name)
 
path = "/var/www/html/youin/file/"#localpath
gobject.threads_init()
wm = WatchManager() 
mask = IN_DELETE|IN_CREATE|IN_MOVED_TO|IN_MOVED_FROM
notifier = ThreadedNotifier(wm, watchfile())
wm.add_watch(path, mask,rec=True)
notifier.start()
 




	
