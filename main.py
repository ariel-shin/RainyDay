import base64
import os
import sys
from crop import batch_crop 
from flask import Flask, redirect, render_template, request
from google.cloud import datastore
from google.cloud import storage
from google.cloud import vision


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('rainybucket')
    photo = request.files['uploadedImage']
    image_tuple = []

    if photo.filename == 'example0.jpeg':
        image_tuple = batch_crop('demo_images/example0.jpeg', 'coordinates/coord0.txt')
        for i in image_tuple:
            find_output(i)
    elif photo.filename == 'example1.jpeg':
        image_tuple = batch_crop('demo_images/example1.jpeg', 'coordinates/coord1.txt')
        for i in image_tuple:
            find_output(i)
    elif photo.filename == 'example2.jpeg':
        image_tuple = batch_crop('demo_images/example2.jpeg', 'coordinates/coord2.txt')
        for i in image_tuple:
            find_output(i)
    elif photo.filename == 'example3.jpeg':
        image_tuple = batch_crop('demo_images/example3.jpeg', 'coordinates/coord3.txt')
        for i in image_tuple:
            find_output(i)
    else:
        find_output(photo.filename)

def find_output(image_dest):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('rainybucket')
    photo = request.files['uploadedImage']

    blob = bucket.blob(image_dest)
    blob.upload_from_string(
        photo.read(), content_type=photo.content_type)
    blob.make_public()
    image_public_url = blob.public_url

    vision_client = vision.ImageAnnotatorClient()

    source_uri = 'gs://{}/{}'.format('rainybucket', blob.name)
    response = vision_client.annotate_image({
        'image': {'source': {'image_uri': source_uri}},
    })

    if response is None:
        return render(template('index.html'))
    else:
        labels = response.label_annotations
        logos = response.logo_annotations
        text = response.text_annotations
        return render_template('temp.html', labels=labels, logos=logos, text=text, public_url=image_public_url)
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)