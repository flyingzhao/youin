#!/usr/bin/python
from socket import *
import os.path
import sys
import time
target = ('121.248.53.183',1234)
def get_header (name):
        leng = len(name)
        assert leng < 250
        return chr(leng) + name

def send_file (name):
        basename = os.path.basename(name)
        header = get_header(basename)
        cont = open(name).read()
        s = socket (AF_INET, SOCK_STREAM)
        s.connect(target)
        s.sendall (header)
        s.sendall (cont)
        s.close()

# for i in sys.argv[1:]:
#         print i
#         send_file (i)
ISOTIMEFORMAT="%Y-%m-%d %X"
print time.strftime( ISOTIMEFORMAT, time.localtime() )
send_file('mixer.zip')
print time.strftime( ISOTIMEFORMAT, time.localtime() )