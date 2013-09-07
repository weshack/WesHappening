from xml.dom import minidom
import urllib2
from bs4 import BeautifulSoup
import datetime
import re

def time_parser(time_string):
    x_to_z = re.compile('[\d]{2}(am|pm).*[\d]{1,2}(am|pm)')
    c1 = x_to_z.findall(p1,re.I)
    print c1
    if c1:
        time = c1[0]
        first = re.compile('[\d]{1,2}')
        start = int(first.findall(time)[0])
        print start
        am_pm = re.compile('(am|pm)')
        to_24 = am_pm.findall(time)[0]
        if to_24 == 'pm':
            start += 12

        end = re.compile

        #make sure to handle an event that has an AM that goes to the next day
        #handle 10:XX - YY:ZZ
        print time


identifiers = {"date":["Date:"],"time":["Time:"],"place":["Place:"]}

# import get_data;get_data.content_parser()

def unicode_hack(unicodey_string):
    """gets all unicode shit out of a string. Hackily"""
    word = ""
    for i in unicodey_string:
        if len(i) == 1:

            word += i
    return word

def content_parser(content,identifiers):
    """
    Content is a list of words and identifiers is a dict of lists
    """

  
    # content = [u'1962.', u'USA.', u'Dir:', u'John', u'Ford.', u'With', u'James', u'Stewart,', u'John', u'Wayne.', u'123', u'min.', u'In', u'a', u'town', u'terrorized', u'by', u'the', u'titular', u'outlaw,', u'an', u'educated', u'lawyer', u'and', u'an', u'individualistic', u'frontiersman', u'strike', u'up', u'uneasy', u'friendship', u'in', u'the', u'name', u'of', u'peace', u'and', u'progress.', u'Western', u'master', u'Ford', u'uses', u'flashbacks', u'to', u'detail', u'a', u'thrilling,', u'cynically', u'self-reflexive', u'commentary', u'on', u'American', u'mythology.', u'Tonight.', u'8pm.', u'Goldsmith', u'Family', u'Cinema.', u'Free.']
    # content = [u'\n', u'From ', u'Keenan Burgess\u201916', u':', u'\n', u'Electronic up-and-comer ', u'Druid Cloak\u2019s', u' coming to Psi U this Saturday for the first party/concert of the fall semester. Wes\u2019 own Ron Beatz and cone+ will be opening.', u'\n', u'Date:', u' Sat, Sept 7', u'\n', u'Time: \xa0', u'9 pm- 2 am', u'\n', u'Place:', u' Psi U', u'\n', u'Cost:', u' FREE', u'\n', u'FB Event.', u'\n']

    info_list = []
    index = 0
    for word in content:
        # print word,"I AM THE WORD"
        for i in identifiers.keys():
            # curr_list = []
            try:
                word = str(word)
                # print word,len(word)
            except:
                word = word.split()[0]
                # print word,"w1"

            e = [str(z) for z in identifiers[i]]
            # print e,"EEEEEEEEEEE",word
            for t in e:
                # print t,word,t in word
                # print len(t),len(word)
                # print [t,word]
                if t in word:
                    # print "MATCH for ",word
                    info_list.append((word,index))
                    break
            # if curr_list:
            #     info_list.append(curr_list)
        index += 1
    if info_list:
        return info_list

def content_builder(content,identifiers,matches):
    """
    Builds list of associated content from list based on given subset/indexes of matches 
    """
    identifiers = {"date":["Date:"],"time":["Time:"],"place":["Place:","Place"]}
    inverse_dict = {}
    for i in identifiers:
        for z in identifiers[i]
            inverse_dict[z] = i

    print inverse_dict,"INVERSE"

    event = {}
    for m in matches:
        if m[0] in inverse_dict:
            


# import get_data;a = get_data.xml_parser();b = get_data.content_parser(a)
def get_xml():
    xml = urllib2.urlopen("http://wesleying.org/feed/")
    dom = minidom.parse(xml)
    items = dom.getElementsByTagName('item')
    return items


# import get_data;get_data.xml_parser()

def xml_parser():
    """FOR WESLEYING"""
    items = get_xml()
    events = []
    # print items,"ITEMS"
    for i in items[0:1]:
        print i,"ITEM"
        title = i.getElementsByTagName('title')[0].childNodes[0].data
        url = i.getElementsByTagName('link')[0].childNodes[0].data
        description = i.getElementsByTagName('description')[0].childNodes[0].data
        content_html = i.getElementsByTagName('content:encoded')[0].childNodes[0].data
        parsed_content = BeautifulSoup(content_html)
        print parsed_content
        try:
            full_description = parsed_content.find('blockquote').text
        except:
            full_description = ""
        # info = parsed_content('p')[3]
        # print info,"INFO"
        # times = ['time']
        # dates = ['date']
        # locations = ['place','where?','location','where']

        event_location = ""
        event_time = ""
        event_date = ""
        # info_str = str(info).lower()
        # print info_str,"INFO STR"
        # print times
        # for t in times:
        #   print t
        #   if t in info_str:
        #       c = re.compile(t+'.*?<.*?<',re.I)
        #       p = c.findall(info_str)[0]
        #       print p,"P!!!!!!!1"
        #       c2 = re.compile('>.*<')
        #       p2 = c2.findall(p)[0][1:-1]
        #       print p2,"P2!!!!!"
        #       event_time = ""
        #       break

        # for t in dates:
        #   if t in info_str:
        #       event_date = t
        #       break

        # for t in locations:
        #   if t in info_str:
        #       event_location = t
        #       break

        # print event_location,event_time,event_date,"Stuff"
        identifiers = {"date":["Date:"],"time":["Time:"],"place":["Place:","Place"]}
        soup = BeautifulSoup(content_html)
        # print '\/n',soup,"SOOOOOOOOOOUP"
        # print "CONTENT",content_html,"END CONTENT"
        info = soup.get_text('|').split('|')
        # print info,"INFO"
        content = content_parser(info,identifiers)
        if content:
            
            ##DO MORE THINGS
            built = content_builder(content)
            event = "those things thing"
        else:
            event = {"title":title,"url":url,"description":description,
                "location":event_location,"time":event_time,
                "date":event_date,"full_description":full_description}

        #HOW THE HELL DO I DO MULTIPLE OPTIONS...
        # p1 = re.compile('Place:.*</p>')
        # p2 = re.compile('WHERE?:.*</p>')

        # z = p1.findall(parsed_content)
        # w = re.compile('>.*<')
        # w.findall(z)[0][1:-1]

        #Check to see if stuff is in the database?

        # event = {"title":title,"url":url,"description":description,
        #         "location":event_location,"time":event_time,
        #         "date":event_date}

        # events.append(event)
        events.append(events)

    return events