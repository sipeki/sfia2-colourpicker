from application import app
import requests

#   This service gets the reponses fro service 2 and 3 and combines
#   the result for synonym and colour.

@app.route('colourpicker', methods=['GET'])
def colourpicked():
    synonym = requests.get('http://service_2:5001/randomsynonym')
    colour = requests.get('http://service_2:5001/randomcolour')
    descriptivecolour = synonym.text + " " + colour.text
    return descriptivecolour