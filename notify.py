#!/usr/bin/python
import dbus
import time
import os
import feedparser
import sys
if(len(sys.argv) < 2):
    print("Usage : python notify.py Kolkata\nUsage : python notify.py India\n")
    exit()
bus = dbus.SessionBus()
notifications = bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')
interface = dbus.Interface(notifications, 'org.freedesktop.Notifications')
id = 4856
i = 0
timeout = 2500
y = sys.argv[1]
cricket_url_rss = "http://static.espncricinfo.com/rss/livescores.xml"
feed = feedparser.parse(cricket_url_rss)
post1 = feed.entries[0]
print("Press Control-C to exit")
for post in feed.entries:
    if(y in post.title):
        post2 = post
        interface.Notify('name',id,'',post.title,'','','',timeout)
        time.sleep(6)
        break
    i = i + 1
while(True):
    if(post2 != post1):
        interface.Notify('name',id,'',post2.title,'','','',timeout)
        time.sleep(6)
        post1 = post2
    feed = feedparser.parse(cricket_url_rss)
    post2 = feed.entries[i]
    
