import spotipy
import spotipy.util as util
import os
from json.decoder import JSONDecodeError


class Remote():
    def __init__(self, username, client_id, client_secret):
        self.username = username
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = 'user-read-private user-read-playback-state user-modify-playback-state'
        self.redirect_uri = 'https://google.com/'
        self.token = None

    def playback(self, device):
        self.__access()
        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            sp.start_playback(device)
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
