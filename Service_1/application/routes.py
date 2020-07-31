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

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    address = db.Column(db.String(150), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(500), nullable=False)



    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
                        'Name: ', self.f_name, ' ', self.l_name, '\r\n',
                        'Email: ', self.email, ' ', self.mobile, '\r\n',
                        'Address: ', self.address, ' ', 'Mobile: ', self.mobile

        ])

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/colourpicker')
    
    colourpicked = response.text
    return render_template('index.html', colourpicked = colourpicked, title = 'Home - Colour Picker')