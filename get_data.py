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
		print parsed_content
		try:
			full_description = parsed_content.find('blockquote').text
		except:
			full_description = ""
		info = parsed_content('p')[3]
		print info,"INFO"
		times = ['time']
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
				c = re.compile(t+'.*?<.*?<',re.I)
				p = c.findall(info_str)[0]
				print p,"P!!!!!!!1"
				c2 = re.compile('>.*<')
				p2 = c2.findall(p)[0][1:-1]
				print p2,"P2!!!!!"
				event_time = ""
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


		soup = BeautifulSoup(content_html)
		soup.find_all("p")[3].get_text('|').split('|')

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