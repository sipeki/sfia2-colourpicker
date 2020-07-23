from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['push', 'get'])
def home():
    response = requests.get('http://localhost:5003/colourtoday')
    print(response)
    colourtoday = response.text
    return render_template('index.html', colourtoday = colourtoday, title = 'Home')