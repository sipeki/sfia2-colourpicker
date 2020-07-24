from application import app
import random

@app.route('/randomsynonym', methods=['GET'])
def beginning():

    synonympositive = ['Ablaze', 'Beaming', 'Bold', 'Bright', 'Brilliant', 'Colorful', 'Dappled', 'Deep', 'Dark', 'Delicate', 'Electric', 'Festive', 'Fiery', 'Flamboyant', 'Flaming', 'Fresh', 'Glistening', 'Glittering', 'Glowing', 'Harmonious', 'Iridescent', 'Jazzy', 'Opalescent', 'Prismatic', 'Radiant', 'Sepia', 'Vibrant', 'Vivid']
    synonymnegative = ['Ashy', 'Bleak', 'Blotchy', 'Brash', 'Chintzy', 'Cold', 'Colorless', 'Dark', 'Dim', 'Discolored', 'Drab', 'Harsh', 'Loud', 'Muddy', 'Opaque', 'Saturated', 'Showy', 'Sickly', 'Somber', 'Sooty', 'Splashy', 'Stained', 'Uneven', 'Washed-out', 'Watery']
    

    if random.randrange(2) == 1:
        synonympicked = synonympositive[random.randrange(len(synonympositive))]
    else:
        synonympicked = synonymnegative[random.randrange(len(synonymnegative))]

    return synonympicked
    