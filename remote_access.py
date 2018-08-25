import spotipy
import spotipy.util as util
import os
from json.decoder import JSONDecodeError
import json


class Remote():
    def __init__(self, username, client_id, client_secret):
        self.username = username
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = 'user-read-private user-read-playback-state user-modify-playback-state'
        self.redirect_uri = 'https://google.com/'
        self.token = None
        self.spotify = self.__access()

    def playback(self, device):
        if self.token:
            self.spotify.start_playback(device)
        else:
            print('Error- Token unavailable')

    def __access(self):
        try:
            self.token = util.prompt_for_user_token(self.username, self.scope,
                                                    self.client_id, self.client_secret,
                                                    self.redirect_uri)

        except (AttributeError, JSONDecodeError):
            os.remove(f".cache-{self.username}")
            self.token = util.prompt_for_user_token(self.username, self.scope,
                                                    self.client_id, self.client_secret,
                                                    self.redirect_uri)
        if self.token:
            return spotipy.Spotify(auth=self.token)
        print('Error- Token unavailable')


    # def get_song_metadata(self):
    #     track = self.spotify.audio_analysis("spotify:album:5nM3cUPxqg7iqjaoyeCWtN")
    #     print(json.dumps(track, indent=4, sort_keys=True))
