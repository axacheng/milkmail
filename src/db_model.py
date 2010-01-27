""" Implements the datastore instances.
"""

from google.appengine.ext import db

class CsvStore(db.Model):
    id = db.IntegerProperty()
    name = db.StringProperty(required=True)
    email = db.TextProperty(required=True)
    item = db.StringProperty(required=True, multiline=True)