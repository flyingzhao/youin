#!/usr/bin/python

import paramiko

targetsocket=("192.168.137.100",22)
user="pi"
pwd="raspberry"
remotepath='/home/pi/youin/123.xls'
localpath='/home/zhao/123.xls'

t = paramiko.Transport(targetsocket)

t.connect(username = user, password = pwd)

sftp = paramiko.SFTPClient.from_transport(t)

sftp.put(localpath,remotepath)

t.close()