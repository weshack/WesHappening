import simplejson
from weshappening import db
from weshappening import Location

f = open("buildings-db.txt", "r")
data = simplejson.load(f)

for key in data:
    building = data[key]
    name = building["name"]
    addr = building["address"]
    location = Location(name, name, addr)
    db.session.add(location)
    db.session.commit()
