#!/usr/bin/python 
#conding:utf-8 
  
import socket,fcntl,struct 
import smtplib
from email.mime.text import MIMEText

def get_ip_address(ifname): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    return socket.inet_ntoa(fcntl.ioctl( 
                s.fileno(), 
                0x8915, # SIOCGIFADDR 
                struct.pack('256s', ifname[:15]) 
                )[20:24]) 
     
print get_ip_address('lo')
print get_ip_address('wlan0')

wlanip=get_ip_address('wlan0')

sender='@qq.com'
receiver='18651267091@sina.cn'
subject='Raspberry Pi IP Addresss'
username='1142749677'
password=''
content='<html><h1>'+wlanip+'</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=subject

smtp=smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
