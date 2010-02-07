
from google.appengine.ext import db
from google.appengine.tools import bulkloader

class CsvStore(db.Model):
    id = db.IntegerProperty()
    MailSent = db.BooleanProperty(default = False)
    Sender = db.EmailProperty()
    Subject = db.StringProperty()
    Recevier = db.EmailProperty()
    Name = db.StringProperty()
    Ntd = db.IntegerProperty()
    Present = db.StringProperty()
    
    
class MilkLoader(bulkloader.Loader):
  def __init__(self):
    bulkloader.Loader.__init__(self, 'CsvStore',
                              [('id', int),
                               ('MailSent', bool),
                               ('Sender', str),
                               ('Subject', lambda x: unicode(x, 'utf-8')),
                               ('Recevier', str),
                               ('Name', lambda x: unicode(x, 'utf-8')),
                               ('Ntd', int),
                               ('Present', lambda x: unicode(x, 'utf-8')),])
                               
loaders = [MilkLoader]

