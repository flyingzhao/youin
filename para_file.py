#!/usr/bin/python

import paramiko

targetsocket=("121.248.53.183",22)
user="pi"
pwd="raspberry"
remotepath='/home/pi/youin/123.pdf'
localpath='/home/zhao/123.pdf'

t = paramiko.Transport(targetsocket)

t.connect(username = user, password = pwd)

sftp = paramiko.SFTPClient.from_transport(t)

sftp.put(localpath,remotepath)

t.close()