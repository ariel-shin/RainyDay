import webapp2
import os
from google.appengine.ext.webapp import template
from google.cloud import vision

class RainyDay(webapp2.RequestHandler):
    def get(self):
        values = 'test vasdlue'
        self.response.out.write(template.render('index.html', values))
    def post(self):
        fileObj = self.request.POST.get('uploadedImage')
        #vision_client = vision.ImageAnnotatorClient()

        # Retrieve a Vision API response for the photo stored in Cloud Storage
        #source_uri = 'gs://{}/{}'.format(os.environ.get('CLOUD_STORAGE_BUCKET'), blob.name)
        #response = vision_client.annotate_image({
        #    'image': {'source': {'image_uri': source_uri}},
        #})
        #labels = response.label_annotations
        #faces = response.face_annotations
        #web_entities = response.web_detection.web_entities

        self.response.out.write('This is a test')

app = webapp2.WSGIApplication([
    ('/', RainyDay),
    ('/upload', RainyDay),
], debug=True)