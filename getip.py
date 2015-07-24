#!/usr/bin/python 
#conding:utf-8 
  
import socket,fcntl,struct 

import urllib
import urllib2

url = 'http://121.248.48.206/youin/process_ip.php'
raspberryid=1

def get_ip_address(ifname): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    return socket.inet_ntoa(fcntl.ioctl( 
                s.fileno(), 
                0x8915, # SIOCGIFADDR 
                struct.pack('256s', ifname[:15]) 
                )[20:24]) 
     


ethip=get_ip_address('eth0')


values = {'ip':ethip,'raspberryid':raspberryid}
data = urllib.urlencode(values)
print data
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page