import webapp2

class RainyDay(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is a <b>test</b>')

app = webapp2.WSGIApplication([
    ('/', RainyDay),
], debug=True)