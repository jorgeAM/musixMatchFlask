from flask import Flask, jsonify, request
from musixmatch.api import Musixmatch

app = Flask(__name__)
API_KEY = '308b70a91756c286c6a18732a4781745'
musixmatch = Musixmatch(API_KEY)

@app.route('/tracks', methods=['POST'])
def get_track():
    lyrics = request.json.get('lyrics')
    track = musixmatch.track.search(lyrics, page_size=1)[0]
    if not lyrics:
        return jsonify({'error': 'Ingresa una parte de la canción que quieres encontrar.'}), 400

    return {
        "res": "La cancion que buscas probablemente es {song} del album {album}"
        .format(song=track.name, album=track.album_name)
    }