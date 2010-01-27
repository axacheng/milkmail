# -*- coding: utf-8 -*-

import datetime
import db_model
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
    

class ShowMailContent(webapp.RequestHandler):
  def get(self):
    query = db_model.CsvStore.all()

    #import sys
    #print >> sys.stdout, query
    self.response.out.write(template.render('ui/show.html', {'query': query}))

class SendMail(webapp.RequestHandler):  
  def get(self):
    pass
  
  def post(self, id):
    pass

class EditContent(webapp.RequestHandler):
  #####db_model.CsvStore.all()
  def get(self, id):
#    key = self.request.get('key')
#    query = db_model.CsvStore.get(key)
    #import sys
    #print >> sys.stdout, 'ccccc'
    query = db_model.CsvStore.all()
    query.filter('id =', int(id))
    self.response.out.write(template.render('ui/edit.html', {'query': query}))
    
    
  def post(self, key):
    key = self.request.get('key') 
    query = db_model.CsvStore.get(key)
    query.item = self.request.get('item')
    query.put()
    self.redirect('/show')
#    key = self.request.get('key')
#    query = db_model.CsvStore.get(key)
#    query.content = self.request.get('content')
#    query.put()
#    self.redirect('/show')
       

def main():
    app = webapp.WSGIApplication([
                                  ('/show', ShowMailContent),
                                  ('/edit/(\d+)', EditContent),
                                  ('/send/(\d+)', SendMail),
                                  ], debug=True)
    run_wsgi_app(app)


if __name__ == "__main__":
    main()