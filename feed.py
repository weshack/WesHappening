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


def no_unicode(string):
    lst = list(string)
    lst2 = lst[:]
    ite = 0
    for i in lst:
        try:
            str(i)
        except:
            print "some damn unicode still in here"
            print ite,lst2[ite],lst2
            lst2.pop(ite)
        ite += 1
    return "".join(lst2)


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
    try:
        date_time,desc = item['description'].split("]",1)
        date_time = date_time.lower()
    except:
        print "COULD NOT GET A DATE_TIME"
        desc = item['description']
        date_time = datetime.datetime.today()
    print date_time

    #match -- [ September 14, 2013; 8:00 PM.
    time = re.search("(:?january|february|march|april|may|june|july|august|september|october|november|december).*\d{1,2}, .*\d{4}.*; \d{1,2}:\d{2}.*to.*\d{1,2}:\d{2}.*(a|p)m(.|;)",date_time)
    if not time:
        time = re.search("(:?january|february|march|april|may|june|july|august|september|october|november|december).*\d{2}, .*\d{4}.*; \d{1}:\d{2}.*(a|p)m(;|.)",date_time)
    if time:
        time = [i.split() for i in time.group().split(".") if i.split()]
        print "TIME!!",time
    else:
        print "NO TIME"
    loc = item["location"]
    print "LOOOO",loc
    if loc:
        ##ADD FOSS HILL TO BUILDINGS.TXT ?
        loc = no_unicode(no_unicode(loc[0]).strip().replace("$","s"))
        print "LOCATION",loc
    else:
        print "NO LOCATION"
    link = str(item['url'])
    # print link

    times = []
    if time:
        for t in time:
            #this catches the weird cases where the next time is a dupe and is 
            # messed up and has no month. 
            if str(t[0]).count(":") == 0:
                month = t[0]
                try:
                    day = int(t[1].split(",")[0])
                except ValueError:
                    day = int(t[1])
                year = int(t[2].split(";")[0])
                z = t[3].split(":")
                hour = int(z[0])
                minutes = int(z[1])

                if t[4] == "pm" and not hour == 12:
                    start_dt = datetime.datetime(year,datetime.datetime.strptime(month,"%B").month,
                        day,hour+12,minutes)
                elif t[4] == "am" and hour == 12:
                    start_dt = datetime.datetime(year,datetime.datetime.strptime(month,"%B").month,
                        day,0,minutes)
                else:
                    start_dt = datetime.datetime(year,datetime.datetime.strptime(month,"%B").month,
                        day,hour,minutes)

                #End time case will be -1 for now
                try:
                    if t[5] == "to":
                        z = t[6].split(":")
                        hour = int(z[0])
                        minutes = int(z[1])

                        if t[7] == "pm" and not hour == 12:
                            end_dt = datetime.datetime(year,datetime.datetime.strptime(month,"%B").month,
                                day,hour+12,minutes)
                        elif t[7] == "am" and hour == 12:
                            end_dt = datetime.datetime(year,datetime.datetime.strptime(month,"%B").month,
                                day,0,minutes)
                        else:
                            end_dt = datetime.datetime(year,datetime.datetime.strptime(month,"%B").month,
                                day,hour,minutes)
                    else: 
                        end_dt = -1

                except IndexError:
                    print "NO END TIME IN THIS TIME",t
                    end_dt = -1

                print start_dt,"to",end_dt
                times.append((start_dt,end_dt))

        print times

    cat = ite % 4
    ite += 1

    if not times:
        times = [[datetime.datetime.today()]]
    event = {"name": name, "location": loc, "time": times[0][0], 
            "link": link, "description": desc, "category":cat}

    print event,"EVENT"
    add_event(event)
    sleep(1)

# logging.debug("Events updated!")
