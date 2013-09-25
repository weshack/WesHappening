import simplejson
from weshappening import db
from weshappening import Location

f = open("buildings.txt", "r")
data = simplejson.load(f)

for key in data:
	try:
		name = key
		addr = data[key]
		location = Location(name, name, addr)
		db.session.add(location)
		db.session.commit()
	except:
		print "DUPLICATE"
		pass