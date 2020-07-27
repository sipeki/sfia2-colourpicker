from application import app
from random import choice

@app.route('/randomcolour', methods=['GET'])
def colour():

    # multidementional array defined
    # first list basic primary colours
    # second list tertiary pastel, metal and secondary colours

    colours = [['White', 'Black', 'Red', 'Yellow', 'Blue'], ['Indigo', 'Magenta', 'Pink', 'Brown', 'Gray', 'Orange', 'Green', 'Violet', 'Purple', 'Silver', 'Gold', 'Platinum']]

    # Randomly selects first or second list of synonyms
    colours = choice(colours)
    
    # Selects synonym from the randomly selected list
    colour = choice(colours)

    return colour

