#!/usr/bin/python
from weshappening import db, Event, Location, delete_event, add_event
from subprocess import call
import logging

path = "/var/www/weshappening/weshappening/weshappening.log"
# logging.basicConfig(filename=path, level=logging.DEBUG,
                        # format="%(asctime)s: %(message)s")
# logging.debug("Cleaning database")

for ev in Event.query.all():
    delete_event(ev.name)

# call(["/var/www/weshappening/weshappening/feed"])

# logging.debug("Database clean!")
