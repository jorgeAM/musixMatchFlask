from flask import Flask, jsonify, request, make_response
from musixmatch.api import Musixmatch

app = Flask(__name__)
API_KEY = '308b70a91756c286c6a18732a4781745'
musixmatch = Musixmatch(API_KEY)

@app.route('/tracks', methods=['POST'])
def get_track():
    req_data = request.get_json(force=True)
    lyrics = req_data.get('queryResult').get('queryText')
    tracks = musixmatch.track.search(lyrics, page_size=1)
    response = ''
    if len(tracks) > 0:
        track = tracks[0]
        response = 'Okay, creo que la cancion es {song}.'.format(song=track.name)
    else:
        response = 'Uy esta esta si esta dificil, mejor probemos con otra.'

    return make_response(jsonify({'fulfillmentText': response}))
