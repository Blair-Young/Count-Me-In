import spotipy
import spotipy.util as util
import os
from json.decoder import JSONDecodeError
import json


username = os.environ['USERNAME']
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
redirect_uri='https://google.com/'

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']


try:
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    devices = sp.devices()

    track = sp.current_playback()
    print(json.dumps(track, indent=4, sort_keys=True))

    phone = '743eb5597fe6dfb1855c40453baced0234e81074'
    laptop = 'b26204cd57cda44dc2890dce9444f7fe07c69ea8'
    # conext_uri = 'spotify:album:2587sGXG2drFrrI4ZS1x0B'
    # sp.start_playback(phone, context_uri=conext_uri, offset= {'position':2} )
    sp.start_playback(phone)
