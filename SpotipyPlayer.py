import spotipy
import spotipy.util as util
from constants import USER_MODIFY_PLAYBACK_SCOPE, USER_READ_PLAYBACK_SCOPE, CONTEXT_URI
import spotify_credentials

class SpotipyPlayer:
    token = ''
    first_available_device_id = ''
    spotipy_instance = ''

    def get_token(self) -> None:
        self.token = util.prompt_for_user_token(
        spotify_credentials.USERNAME, 
        f'{USER_MODIFY_PLAYBACK_SCOPE}%20{USER_READ_PLAYBACK_SCOPE}',
        spotify_credentials.CLIENT_ID, 
        spotify_credentials.CLIENT_SECRET,
        spotify_credentials.REDIRECT_URI)

    def initialize_spotipy_to_get_first_available_device(self) -> None:
        self.spotipy_instance = spotipy.Spotify(self.token)
        avaliable_devices = self.spotipy_instance.devices()
        self.first_available_device_id = avaliable_devices['devices'][0]['id']

    def start_playback(self) -> None:
        self.spotipy_instance.start_playback(self.first_available_device_id,
        CONTEXT_URI)

    def repeat_playback(self, state = 'context') -> None:
        self.spotipy_instance.repeat(state, self.first_available_device_id)

    def shuffle_playback(self, state: bool = True) -> None:
        self.spotipy_instance.shuffle(state, self.first_available_device_id)