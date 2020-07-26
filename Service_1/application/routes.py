from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/colourpicker')
    
    colourpicked = response.text
    return render_template('index.html', colourpicked = colourpicked, title = 'Home - Colour Picker')