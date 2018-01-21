import webapp2
import os
from google.appengine.ext.webapp import template

class RainyDay(webapp2.RequestHandler):
    def get(self):
        values = 'test vasdlue'
        self.response.out.write(template.render('index.html', values))

app = webapp2.WSGIApplication([
    ('/', RainyDay),
], debug=True)