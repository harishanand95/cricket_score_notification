#!/usr/bin/python
import dbus         #for notification
import time
import feedparser
import sys
import os
import copy
class bcolors:
    OKBLUE = '\033[94m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
os.system('clear')
#notification for desktop, are configured
bus = dbus.SessionBus()
notifications = bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')
interface = dbus.Interface(notifications, 'org.freedesktop.Notifications')
id = 4856
i = 0
timeout = 2500
cricket_url_rss = "http://static.espncricinfo.com/rss/livescores.xml"
feed = feedparser.parse(cricket_url_rss)
if(feed.entries == []):
    print("No Internet Connection Found or No live matches")
    interface.Notify('name',id,'',"No Internet Connection Found or No live matches",'','','',timeout)
    exit()
print bcolors.OKBLUE + "\n\tESPNCRICINFO" + bcolors.ENDC
print bcolors.YELLOW + "\tSelect Team and Notification's will be provided in Desktop\n\n" + bcolors.ENDC
print "\tLink : http://static.espncricinfo.com/rss/livescores.xml\n\nLive Games:\n"

for post1 in feed.entries:
    print"{}.".format(i+1)  
    print(post1.title)
    print("\n")
    i = i + 1
print("Enter option no. of the live game:")
x = input("Enter a number: ")
flag = 0
if(x>(i) or x<1):
    print "\nWrong Option.Exiting"
    exit()

print "Score Updates are based only on espncricinfo RSS site\nPress Control-C (Keyboard Interupt) to exit"
Compare = ""
post = feed.entries[x-1]
while(True):
    if(Compare == "" or post.title != Compare):
        if(Compare == "" or (post.title > Compare)):
            interface.Notify('name',id,'',post.title,'','','',timeout)
    time.sleep(6)
    Compare = copy.deepcopy(post.title)
    #post2.title = copy.deepcopy(post1.title)
    print Compare + "\n"
    feeder = feedparser.parse(cricket_url_rss)
    if(feeder.entries == []):
        time.sleep(10) #waits more time to make sure of connection
        feeder = feedparser.parse(cricket_url_rss)
        if(feeder.entries == []):
            print("Internet Connection Lost")
            interface.Notify('name',id,'',"Internet Connection Lost",'','','',timeout)
            exit()
    post = feeder.entries[x-1]
    
