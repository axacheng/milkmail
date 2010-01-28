# -*- coding: utf-8 -*-
import db_model

from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
    

class ShowMailContent(webapp.RequestHandler):
  """ Show list of mail content to index page.
  """
  def get(self):
    """Return the query result from CsvStore model.
    
    I use 'p' as request argument. 
    You can get unfiltered result if parameter == 'all'. The default query 
    result would be filtered by 'MailSent' column equl False. 
    """
    query = db_model.CsvStore.all()
    p = self.request.get('p')
    if p == 'all':
      self.response.out.write(template.render('ui/show.html', {'query': query}))
    else:
      query.filter('MailSent =', False)
      self.response.out.write(template.render('ui/show.html', {'query': query}))


class SendMail(webapp.RequestHandler):
  """ Send out mail from html template with CsvStore factors. 
  
  SMPT server will be defined at dev_appserver.py with --smtp_host option.
  As long as, you filled out correct receiver mail address then we can go.
  """
  def get(self):
    pass
  
  def post(self, id):
    """ Send mail out to receiver with given form 'id' from POST method of html 
    template <form> (aka: mail_template.html). Actually, the 'id' value 
    would come from jquery $.ajax of url: method.
    
    Args:
      id = The id from html form POST argument (ex:/send/8)
    
    Returns:
      jquery %.ajax success() method return
    """  
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
#      message.sender = sender
#      message.to = receiver
      #message.sender = '172.19.104.250'
      #message.to = 'axanet@ms32.hinet.net'
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
    
    message.send() ### send mail out

    for mail_stat in query:
      mail_stat.MailSent = True  ### Set boolean to 'True' meant mail has been
                                 ### out to receiver.
      mail_stat.put() ### commit change to db.Csvstore(aka: query) object.


class EditContent(webapp.RequestHandler):
  """ Allow user can edit .csv file content with browser
  
  You can edit your datasource(aka:.csv) file if you wanted.
  """
  def get(self, id):
    """ Edit page for .csv file adjustment.
    
    Args: 
      string, given button of document.location.href {{ mesg.id }} from html.
    
    Returns:
      CsvStore query result to edit.html template
    """
    query = db_model.CsvStore.all()
    query.filter('id =', int(id))
    self.response.out.write(template.render('ui/edit.html', {'query': query}))
    
    
  def post(self, key):
    """ Save adjustment back to datastore
    
    Args:
      string, given {{ query.key }} from  edit.html <form>
    
    Return:
      Redirect page to /show
    """
    key = self.request.get('key') 
    query = db_model.CsvStore.get(key)
    query.Present = self.request.get('present')
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