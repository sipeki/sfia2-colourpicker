from application import app
import requests

#   This service gets the reponses from service 2 synonym and 3 colour and combines
#   the result for synonym and colour.

@app.route('/colourpicker', methods=['GET'])
def colourpicked():
    # synonym = requests.get('http://service_2:5001/randomsynonym')
    # colour = requests.get('http://service_3:5002/randomcolour')

    synonym = requests.get('http://localhost:5001/randomsynonym')
    colour = requests.get('http://localhost:5002/randomcolour')

    response = synonym.text + " " + colour.text
    return response