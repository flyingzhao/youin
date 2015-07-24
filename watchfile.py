#!/usr/bin/env python
#coding=utf-8
 
import os
import gobject
from  pyinotify import  WatchManager, Notifier, ProcessEvent, ThreadedNotifier, IN_DELETE, IN_CREATE,IN_MOVED_TO,IN_MOVED_FROM
 
class watchfile(ProcessEvent):
    def process_IN_CREATE(self, event):
        print   "创建文件: %s "  %   os.path.join(event.path, event.name)
 
    def process_IN_DELETE(self, event):
        print   "删除文件: %s "  %   os.path.join(event.path, event.name)
 
    def process_IN_MOVED_TO(self, event):
        print   "移来文件: %s "  %   os.path.join(event.path, event.name)
 
    def process_IN_MOVED_FROM(self, event):
        print   "移走文件: %s "  %   os.path.join(event.path, event.name)
 
path = "/home/zhao/youin/"
gobject.threads_init()
wm = WatchManager() 
mask = IN_DELETE|IN_CREATE|IN_MOVED_TO|IN_MOVED_FROM
notifier = ThreadedNotifier(wm, watchfile())
wm.add_watch(path, mask,rec=True)
notifier.start()
 
