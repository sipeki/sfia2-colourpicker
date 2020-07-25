from application import app
from random import choice

@app.route('/randomsynonym', methods=['GET'])
def synonym():

    # multidementional array define
    # first list synonym positive
    # second list synonym negative

    synonyms = [['Ablaze', 'Beaming', 'Bold', 'Bright', 'Brilliant', 'Colorful', 'Dappled', 'Deep', 'Dark', 'Delicate', 'Electric', 'Festive', 'Fiery', 'Flamboyant', 'Flaming', 'Fresh', 'Glistening', 'Glittering', 'Glowing', 'Harmonious', 'Iridescent', 'Jazzy', 'Opalescent', 'Prismatic', 'Radiant', 'Sepia', 'Vibrant', 'Vivid'], ['Ashy', 'Bleak', 'Blotchy', 'Brash', 'Chintzy', 'Cold', 'Colorless', 'Dark', 'Dim', 'Discolored', 'Drab', 'Harsh', 'Loud', 'Muddy', 'Opaque', 'Saturated', 'Showy', 'Sickly', 'Somber', 'Sooty', 'Splashy', 'Stained', 'Uneven', 'Washed-out', 'Watery']]

    # Randomly selects first or second list of synonyms
    synonyms = choice(synonyms)

    # Selects synonym from the randomly selected list
    synonym = choice(synonyms)

    return synonym

    