from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from pygeocoder import Geocoder
import simplejson

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/events.db'
db = SQLAlchemy(app)

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship('Location') 
    time = db.Column(db.DateTime)
    link = db.Column(db.String(200))
    description = db.Column(db.Text)
    category = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __init__(self, name, location, time, link, description, category, lat=0.0, lon=0.0):
        self.name = name
        self.location = location
        self.time = time
        self.link = link
        self.description = description
        self.category = category
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return '<Event %s>' % self.name


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    short_name = db.Column(db.String(50))
    addr = db.Column(db.String(100))

    def __init__(self, name, short_name, addr):
        self.name = name
        self.short_name = short_name
        self.addr = addr

    def __repr__(self):
        return '<Location %s>' % self.name


def serialize(locs):
    locations = []
    for loc in locs:
       l = {'name': loc.name}
       locations.append(l)
    return simplejson.dumps(locations)

        
def serialize_events(events):
    evs = []
    for event in events:
        time = '%s,%s,%s,%s,%s' % (event.time.year, event.time.month, event.time.day, event.time.hour, event.time.minute)

        ev = {'name': event.name, 'location': serialize([event.location]),
              'time': time, 'link': event.link,
              'description': event.description,
              'lat': event.lat, 'lon': event.lon,
              'category': event.category}
        evs.append(ev)
    return simplejson.dumps(evs)


def query_name(pattern, d):
    if d == "location":
        locs = Location.query.all()
        l = []
        for loc in locs:
            if not (loc.name.find(pattern) == -1):
                l.append(loc)
        if not (len(l) == 0):
            return l
    elif d == "event":
        evs = Event.query.all()
        e = []
        for ev in evs:
            if not (ev.name.find(pattern) == -1):
                e.append(ev)
        if not (len(l) == 0):
            return e
    else:
        return None

@app.route('/')
def index():
#  locations = simplejson.dumps(Location.query.all())
  locations = serialize(Location.query.all())
  #events = ['option_1','option_2','option_3','option_4']
  events = serialize_events(Event.query.all())
  categories = ['cat 1','cat 2','cat 3']
  return render_template("index.html", locations = locations, events = events, categories = categories)


def add_event(event):
    name = event["name"]
    if not Event.query.filter_by(name=name).first():
        loc = event["location"]
        #location = Location.query.filter(Location.name.startswith(loc)).first()
        location = query_name(loc.split(" ")[0], "location")
        print location
        if not location:
            loc = Location.query.filter_by(name="Unknown").first()
            lat, lon = (0.0, 0.0)
        else:
            loc = location[0]
            lat, lon = Geocoder.geocode(loc.name + ", Middletown, CT, 06457").coordinates
        time = event["time"]
        link = event["link"]
        desc = event["description"]
        cat = event["category"]
        ev = Event(name, loc, time, link, desc, cat, lat, lon)
        db.session.add(ev)
        db.session.commit()

def delete_event(event):
    ev = Event.query.filter_by(name=event).first()
    if ev:
        db.session.delete(ev)
        db.session.commit()

if __name__ == "__main__":
  app.debug = True
  app.run()
