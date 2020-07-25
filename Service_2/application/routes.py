from application import app
import random

@app.route('/randomsynonym', methods=['GET'])
def synony():

    # multidementional array define
    # first list synonym positive
    # second list synonym negative

    synonyms = [['Ablaze', 'Beaming', 'Bold', 'Bright', 'Brilliant', 'Colorful', 'Dappled', 'Deep', 'Dark', 'Delicate', 'Electric', 'Festive', 'Fiery', 'Flamboyant', 'Flaming', 'Fresh', 'Glistening', 'Glittering', 'Glowing', 'Harmonious', 'Iridescent', 'Jazzy', 'Opalescent', 'Prismatic', 'Radiant', 'Sepia', 'Vibrant', 'Vivid'], ['Ashy', 'Bleak', 'Blotchy', 'Brash', 'Chintzy', 'Cold', 'Colorless', 'Dark', 'Dim', 'Discolored', 'Drab', 'Harsh', 'Loud', 'Muddy', 'Opaque', 'Saturated', 'Showy', 'Sickly', 'Somber', 'Sooty', 'Splashy', 'Stained', 'Uneven', 'Washed-out', 'Watery']]

    # Selects first or second list
    synonympicked = random.choice(synonyms)
    synonympicked = random.choice(synonympicked)

    return synonympicked

    