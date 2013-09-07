from xml.dom import minidom
import urllib2
from BeautifulSoup import BeautifulSoup
import datetime
import re

def xml_parser():
	"""FOR WESLEYING"""
	xml = urllib2.urlopen("http://wesleying.org/feed/")
	dom = minidom.parse(xml)
	items = dom.getElementsByTagName('item')
	events = []
	print items,"ITEMS"
	for i in items:
		print i,"ITEM"
		title = i.getElementsByTagName('title')[0].childNodes[0].data
		url = i.getElementsByTagName('link')[0].childNodes[0].data
		description = i.getElementsByTagName('description')[0].childNodes[0].data
		content_html = i.getElementsByTagName('content:encoded')[0].childNodes[0].data
		parsed_content = BeautifulSoup(content_html)
		full_description = parsed_content.find('blockquote').text

		info = parsed_content('p')[3]
		print info,"INFO"
		times = ['time']
		print type(times)
		dates = ['date']
		locations = ['place','where?','location','where']

		event_location = ""
		event_time = ""
		event_date = ""
		info_str = str(info).lower()
		print info_str,"INFO STR"
		print times
		for t in times:
			print t
			if t in info_str:
				event_time = t
				break

		for t in dates:
			if t in info_str:
				event_date = t
				break

		for t in locations:
			if t in info_str:
				event_location = t
				break

		print event_location,event_time,event_date,"Stuff"

		#HOW THE HELL DO I DO MULTIPLE OPTIONS...
		# p1 = re.compile('Place:.*</p>')
		# p2 = re.compile('WHERE?:.*</p>')

		# z = p1.findall(parsed_content)
		# w = re.compile('>.*<')
		# w.findall(z)[0][1:-1]

		#Check to see if stuff is in the database?

		event = {"title":title,"url":url,"description":description,
				"location":event_location,"time":event_time,
				"date":event_date}

		events.append(event)

	return events