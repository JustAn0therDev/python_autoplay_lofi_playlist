import spotipy
import spotipy.util as util
import spotify_credentials

class Spotipy_Player:
    scope = 'user-modify-playback-state'
    scope_two = 'user-read-playback-state'
    context_uri_lofi_playlist = 'spotify:playlist:74sUjcvpGfdOvCHvgzNEDO'
    token = ''
    first_available_device_id = ''
    spotipy_instance = ''

    def get_token(self) -> None:
        self.token = util.prompt_for_user_token(
        spotify_credentials.USERNAME, 
        f'{self.scope}%20{self.scope_two}',
        spotify_credentials.CLIENT_ID, 
        spotify_credentials.CLIENT_SECRET,
        spotify_credentials.REDIRECT_URI)

    def initalize_spotipy(self) -> None:
        self.spotipy_instance = spotipy.Spotify(self.token)

    def get_first_available_device(self) -> None:
        avaliable_devices = self.spotipy_instance.devices()
        self.first_available_device_id = avaliable_devices['devices'][0]['id']

    def start_playback(self) -> None:
        self.spotipy_instance.start_playback(self.first_available_device_id, self.context_uri_lofi_playlist)

    def repeat_playback(self, state: str) -> None:
        self.spotipy_instance.repeat(state, self.first_available_device_id)

    def shuffle_playback(self, state: bool) -> None:
        self.spotipy_instance.shuffle(state, self.first_available_device_id)