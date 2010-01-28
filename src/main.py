# -*- coding: utf-8 -*-

import datetime
import db_model

from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
    

class ShowMailContent(webapp.RequestHandler):
  def get(self):
    query = db_model.CsvStore.all()
    p = self.request.get('p')
    if p == 'all':
      self.response.out.write(template.render('ui/show.html', {'query': query}))
    else:
      query.filter('MailSent =', False)
      self.response.out.write(template.render('ui/show.html', {'query': query}))


class SendMail(webapp.RequestHandler):  
  def get(self):
    pass
  
  def post(self, id):  
    #key = db.GqlQuery("SELECT __key__ "
    #                    "FROM CsvStore "
    #                    "WHERE id = :gql_id", gql_id=id).get()
    query = db_model.CsvStore.all().filter('id =', int(id))
  
    for result in query:
      id = result.id
      sender = result.Sender
      receiver = result.Recevier
      subject = result.Subject
      name = result.Name
      present = result.Present
     
    params = {'id':id, 'sender':sender, 'receiver':receiver, 'subject':subject,
              'name':name, 'present':present}   
#    try:
#      message = mail.EmailMessage()
#      #message.sender = sender
#      #message.to = receiver
#      message.sender = '172.19.104.250'
#      message.to = 'axanet@ms32.hinet.net'
#      message.subject = subject
#      message.html = (template.render('ui/mail_template.html', params)) 
#      message.check_initialized()

#    except mail.InvalidEmailError:
#      self.handle_error('Invalid email recipient.')
#      return
#    except mail.MissingRecipientsError:
#      self.handle_error('You must provide a recipient.')
#      return
#    except mail.MissingBodyError:
#      self.handle_error('You must provide a mail format.')
#      return

#    message.send()
    for mail_stat in query:
      mail_stat.MailSent = True
      mail_stat.put()



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
       

def main():
    app = webapp.WSGIApplication([
                                  ('/show', ShowMailContent),
                                  ('/edit/(\d+)', EditContent),
                                  ('/send/(\d+)', SendMail),
                                  ], debug=True)
    run_wsgi_app(app)


if __name__ == "__main__":
    main()