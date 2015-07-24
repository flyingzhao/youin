#!/usr/bin/python

import paramiko

 

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.137.100",22,"pi", "raspberry")

stdin, stdout, stderr = ssh.exec_command("ls")

print stdout.readlines()

ssh.close()