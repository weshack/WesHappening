import json
from weshappening import db
from weshappening import Location

f = open("buildings-db.txt", "r")
data = json.load(f)

for key in data:
    building = data[key]
    name = building["name"]
    addr = building["address"]
    lat = building["lat"]
    lon = building["lon"]
    location = Location(name, name, lat, lon, addr)
    db.session.add(location)
    db.session.commit()
