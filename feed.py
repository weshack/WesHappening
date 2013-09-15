#!/usr/bin/python
import feedparser
import re
import datetime
from weshappening import add_event
from get_data import xml_parser
from time import sleep
import logging


# path = "/var/www/weshappening/weshappening/weshappening.log"
# logging.basicConfig(filename=path, level=logging.DEBUG,
#                         format="%(asctime)s: %(message)s")
# logging.debug("Updating events")

feed_url = "http://events.wesleyan.edu/events/cal_rss_today"

feed = feedparser.parse(feed_url)

wesleying_feed = xml_parser()


# ite = 0
# for item in feed["items"]:
#     name = str(item["title"])
#     if name.startswith("TBA"):
#         name = name[4:]
#     else:
#         name = name[9:]
#     value = item["summary_detail"]["value"].split("<br />")
#     date = re.match("\d\d/\d\d/\d\d\d\d", str(value[0])).group().split("/")
#     time = re.search("(TBA|\d\d:\d\d (a|p)m( - \d\d:\d\d (a|p)m)*)", str(value[0])).group().split(" ")
#     desc = value[0]
#     loc = re.search("Location: .*", str(value[-1])).group().lstrip("Location: ")
#     link = ""
#     for v in value:
#         if v.startswith("URL"):
#             link = v.lstrip("URL: ")

#     if len(time) > 1:
#         t = time[0].split(":")
#         if (time[1] == "pm") and not (int(t[0]) == 12):
#             dt = datetime.datetime(int(date[2]), int(date[0]), int(date[1]), (int(t[0])+12)%24, int(t[1]))
#         elif (int(t[0]) == 12) and (t[1] == ("am")):
#             dt = datetime.datetime(int(date[2]), int(date[0]), int(date[1]), 0, int(t[1]))
#         else:
#             dt = datetime.datetime(int(date[2]), int(date[0]), int(date[1]), int(t[0]), int(t[1]))
#     else:
#         dt = datetime.datetime(int(date[2]), int(date[0]), int(date[1]))

#     cat = ite % 4
#     ite += 1

#     event = {"name": name, "location": loc, "time": dt, "link": link, "description": desc, "category":cat}

#     add_event(event)
#     sleep(1)

def u_to_string(string):
    return eval('"' + string.replace('"','') + '"')

##FOR WESLEYING
ite = 0
# print wesleying_feed
for item in wesleying_feed:
    name = item["title"]
    # if item["date"]:
    #     date = u_to_string(item["date"][0])
    # else:
    #     print "NO DATE"
    #(:?january|february|march|april|may|june|july|august|september|october|november|december).* \d{2}, .*\d{4}.*; \d{1}:\d{2}.*to.*\d{1}:\d{2}.*(a|p)m.

    # if item["time"]:
    #     time = re.search("(TBA|\d\d:\d\d (a|p)m( - \d\d:\d\d (a|p)m)*)", u_to_string(item['time'][0]))
    #     time = u_to_string(item["time"][0]).lower().strip()
    #     print time,"HAVE TIME"
    # else:
    #     print "NO TIME"
    #this removes some unicode characters that I can't
    #seem to convert to ascii. Therefore grammar=messy
    try:
        date_time,desc = item['description'].split("]",1)
        date_time = date_time.lower()
    except:
        print "COULD NOT GET A DATE_TIME"
        desc = item['description']
        date_time = datetime.datetime.today()
    # print date_time

    #match -- [ September 14, 2013; 8:00 PM.
    time = re.search("(:?january|february|march|april|may|june|july|august|september|october|november|december).*\d{1,2}, .*\d{4}.*; \d{1,2}:\d{2}.*to.*\d{1,2}:\d{2}.*(a|p)m(.|;)",date_time)
    if not time:
        time = re.search("(:?january|february|march|april|may|june|july|august|september|october|november|december).*\d{2}, .*\d{4}.*; \d{1}:\d{2}.*(a|p)m(;|.)",date_time)
    if time:
        print "TIME!!",[i.split() for i in time.group().split(".") if i.split()]
    else:
        print "NO TIME"
    loc = item["location"]
    if loc:
        ##ADD FOSS HILL TO BUILDINGS.TXT ?
        loc = u_to_string(loc[0]).strip().replace("$","s")
        # print "LOCATION",loc
    else:
        print "NO LOCATION"
    link = str(item['url'])

    try:

        if len(time) > 1:
            t = time[0].split(":")
            if (time[1] == "pm") and not (int(t[0]) == 12):
                dt = datetime.datetime(int(date[2]), int(date[0]), int(date[1]), (int(t[0])+12)%24, int(t[1]))
            elif (int(t[0]) == 12) and (t[1] == ("am")):
                dt = datetime.datetime(int(date[2]), int(date[0]), int(date[1]), 0, int(t[1]))
            else:
                dt = datetime.datetime(int(date[2]), int(date[0]), int(date[1]), int(t[0]), int(t[1]))
        else:
            dt = datetime.datetime(int(date[2]), int(date[0]), int(date[1]))
    except:
    #    print "nope"
        pass
    cat = ite % 4
    ite += 1
    
    event = {"name": name, "location": loc, "time": datetime.datetime.today() , 
            "link": link, "description": desc, "category":cat}

    #print event,"EVENT"
    add_event(event)
    sleep(1)

# logging.debug("Events updated!")
