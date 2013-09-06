from pygeocoder import Geocoder
import time
import json

f = open("buildings.txt", 'r')
build = json.load(f)
buildings = {}
for key in build:
    v = build[key]
    print key, v
    lat, lon = Geocoder.geocode(v + ", Middletown, CT, 06457")[0].coordinates
    print lat, lon
    buildings[key] = {"name": key, "address": v, "lat": lat, "lon": lon}
    time.sleep(1)

print buildings
o = open("buildings-db.txt", "w")
o.write(json.dumps(buildings))
o.close
f.close
