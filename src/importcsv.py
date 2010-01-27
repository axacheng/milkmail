
from google.appengine.ext import db
from google.appengine.tools import bulkloader

class CsvStore(db.Model):
    id = db.IntegerProperty()
    name = db.StringProperty(required=True)
    email = db.TextProperty(required=True)
    item = db.StringProperty(required=True, multiline=True)
    
    
class MilkLoader(bulkloader.Loader):
  def __init__(self):
    bulkloader.Loader.__init__(self, 'CsvStore',
                              [('id', int),
                               ('name', lambda x: unicode(x, 'utf-8')),
                               ('email', str),
                               ('item', lambda x: unicode(x, 'utf-8')),])
loaders = [MilkLoader]

