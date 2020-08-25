from application import app
import requests

#   This service gets the reponses from service 2 synonym and 3 colour and combines
#   the result for synonym and colour.

@app.route('/colourpicker', methods=['GET'])
def colourpicked():
    # request API on port 5001 & 5002 for returned string
    synonym = requests.get('http://service-2:5001/randomsynonym')
    colour = requests.get('http://service-3:5002/randomcolour')

    # concatenates responses 
    response = synonym.text + " " + colour.text
    return response