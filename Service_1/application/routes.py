from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
from datetime import datetime

import requests
import random

app = Flask(__name__)

# Pass database security settings through OS environment

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_PRJ_DB_NAME')

db = SQLAlchemy(app)

class ColourPicker(db.Model):
    ColourID = db.Column(db.Integer, primary_key=True)
    ColourPicked = db.Column(db.String(255), nullable=False)
    User = db.Column(db.String(255), nullable=True)
    ColourCreated =  db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    
    def __repr__(self):
        return ''.join(
            [
                'Stock ID:  ' + self.stock_id + ' Detail:  ' + self.detail + ' Price: £' + self.price + '\n'
            ]
        )

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/colourpicker')
    
    colourpicked = response.text
    return render_template('index.html', colourpicked = colourpicked, title = 'Home - Colour Picker')