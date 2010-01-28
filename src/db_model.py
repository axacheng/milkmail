""" Implements the datastore instances.
"""

from google.appengine.ext import db

class CsvStore(db.Model):
    id = db.IntegerProperty()
    MailSent = db.BooleanProperty(default = False)
    Sender = db.EmailProperty()
    Subject = db.StringProperty()
    Activity = db.StringProperty()
    Month = db.StringProperty()
    Recevier = db.EmailProperty()
    Name = db.StringProperty()
    Duration = db.StringProperty()
    Present = db.StringProperty()
    Publish = db.StringProperty()