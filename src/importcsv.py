
from google.appengine.ext import db
from google.appengine.tools import bulkloader

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
    
    
class MilkLoader(bulkloader.Loader):
  def __init__(self):
    bulkloader.Loader.__init__(self, 'CsvStore',
                              [('id', int),
                               ('MailSent', bool),
                               ('Sender', str),
                               ('Subject', lambda x: unicode(x, 'utf-8')),
                               ('Activity', lambda x: unicode(x, 'utf-8')),
                               ('Month', str),
                               ('Recevier', str),
                               ('Name', lambda x: unicode(x, 'utf-8')),
                               ('Duration', str),
                               ('Present', lambda x: unicode(x, 'utf-8')),
                               ('Publish', str),])
                               
loaders = [MilkLoader]

