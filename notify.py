#!/usr/bin/python
import dbus         #for notification
import time
import feedparser
import sys
import os
from bs4 import BeautifulSoup
import copy
import urllib
from lxml import html

def scorecard(strr,soup):
    output = ""
    str = "    "
    j = 0
    for string in soup.stripped_strings:
        if  "End of over" in  string:
            str = string
            j = 0
        if(j == 0):
            output = ""
            output += string
            j += 1
        elif(j != 12):
            output += string + "  "
            j = j + 1
    if(str == strr):
        return False
    else:
        return output
    

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
#    interface.Notify('name',id,'',"No Internet Connection Found or No live matches",'','','',timeout)
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
flag = 1

if(x>(i) or x<1):
    print "\nWrong Option.Exiting"
    exit()
flag = input("\nSelect the innings(by default \"1\" which is first innings will be displayed) : ")
if(flag >4 or flag <1):
    print "\nWrong Option.Exiting"
    exit()
url =  feed.entries[x-1].id + "?innings="+ str(flag) +";view=commentary;wrappertype=none"
page = urllib.urlopen(url).read()
soup = BeautifulSoup(page)
print bcolors.OKBLUE+ "\n\tIf the score isn't displayed properly, please make sure that the provided innings is correct.\n\tA T20 and ODI match has 2 innings and a Test match has 4 innings" + bcolors.ENDC
output1 = scorecard("QWERTY",soup)
output = output1
interface.Notify("name",id,'',str(output1),'','','',timeout)
while True:
    
    output1 = output
    output1 = output.split('(',1)
    output1 = output1[0]
    output1 = scorecard(output1,soup)
   
    if output1 != False: 
        interface.Notify("name",id,'',str(output1),'','','',timeout)
        output = output1
    time.sleep(10)
    page = urllib.urlopen(url).read()
    soup = BeautifulSoup(page)



    
    

