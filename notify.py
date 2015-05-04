#!/usr/bin/python
import dbus
import time
import os
import feedparser

if(len(sys.argv) < 2):
    print("Usage : python notify.py Kolkata\nUsage : python notify.py India\n")
    exit()
bus = dbus.SessionBus()
notifications = bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')
interface = dbus.Interface(notifications, 'org.freedesktop.Notifications')
id = 4856
timeout = 2500
y = sys.argv[1]
cricket_url_rss = "http://static.espncricinfo.com/rss/livescores.xml"
feed = feedparser.parse(cricket_url_rss)
post1 = feed.entries[0]
print("Press Control-C to exit")
while(True):
    for post in feed.entries:
        if(y in post.title and post != post1):
            interface.Notify('name',id,'',post.title,'','','',timeout)
            time.sleep(20)
            post1 = post
            feed = feedparser.parse(cricket_url_rss)

    
