from flask import Flask, request
import requests

app = Flask(__name__)

from application import routes