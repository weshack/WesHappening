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
    name = db.Column(db.String(100))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship('Location') 
    time = db.Column(db.DateTime)
    link = db.Column(db.String(100))
    description = db.Column(db.Text)
    category = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __init__(self, name, location, time, link, description, category):
        self.name = name
        self.location = location
        self.time = time
        self.link = link
        self.description = description
        self.category = category

    def __repr__(self):
        return '<Event %s>' % self.name


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
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
       l = {'name': loc.name, 'lat': 41.556, 'lon': -72.6576}
       locations.append(l)
    return simplejson.dumps(locations)

@app.route('/')
def index():
#  locations = simplejson.dumps(Location.query.all())
  locations = serialize(Location.query.all())
  events = ['option_1','option_2','option_3','option_4']
  categories = ['cat 1','cat 2','cat 3']
  return render_template("index.html", locations = locations, events = events, categories = categories)


def add_event(event):
    name = event["name"]
    loc = event["location"]
    location = Location.query.filter_by(name=loc).first()
    if not location:
        location = Location.query.filter_by(name="Undefined").first()
        lat, lon = (0.0, 0.0)
    else:
        lat, lon = Geocoder.geocode(location.name + ", Middletown, CT, 06457").coordinates
    time = event["time"]
    link = event["link"]
    desc = event["description"]
    cat = event["category"]
    ev = Event(name, location, time, link, desc, cat)
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
