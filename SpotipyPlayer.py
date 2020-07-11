import spotipy
import spotify_credentials
from spotipy import Spotify
from Token import Token

class SpotipyPlayer:
    first_available_device_id = ''
    spotipy_instance: Spotify = None

    def play(self, context_uri: str, repeat: bool = False, shuffle: bool = False):
        self.__initialize_spotipy()
        self.__get_first_available_device()
        self.__start_playback(context_uri)
        if repeat:
            self.__repeat_playback()
        if shuffle:
            self.__shuffle_playback()

    def __initialize_spotipy(self) -> None:
        self.spotipy_instance = spotipy.Spotify(Token.get_token())

    def __get_first_available_device(self) -> None: 
        avaliable_devices = self.spotipy_instance.devices()
        self.first_available_device_id = avaliable_devices['devices'][0]['id']

    def __start_playback(self, context_uri: str) -> None:
        self.spotipy_instance.start_playback(self.first_available_device_id, context_uri)

    def __repeat_playback(self, state: str = 'context') -> None:
        self.spotipy_instance.repeat(state, self.first_available_device_id)

    def __shuffle_playback(self, toggle: bool = True) -> None:
        self.spotipy_instance.shuffle(toggle, self.first_available_device_id)