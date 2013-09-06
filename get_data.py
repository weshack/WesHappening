from xml.dom import minidom
import urllib2

def xml_parser():
	xml = urllib.urlopen("http://wesleying.org/feed/")
	dom = parse(xml)
	items = dom.getElementsByTagName('item')
	for i in items:
		title = i.childNodes[1].childNodes[0].data