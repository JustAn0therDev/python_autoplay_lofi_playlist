import spotipy
import spotipy.util as util
import time
import spotify_credentials

scope = 'user-modify-playback-state'
scope_two = 'user-read-playback-state'
context_uri_lofi_playlist = 'spotify:playlist:74sUjcvpGfdOvCHvgzNEDO'
token = util.prompt_for_user_token(spotify_credentials.username, f'{scope}%20{scope_two}',spotify_credentials.CLIENT_ID, spotify_credentials.CLIENT_SECRET, 'http://localhost:3333/')

try:
    sp = spotipy.Spotify(auth=token)

    available_devices = sp.devices()
    first_available_device_id = available_devices['devices'][0]['id']

    sp.start_playback(first_available_device_id, context_uri_lofi_playlist)

    sp.repeat('context', first_available_device_id)
except Exception as error_message:
    print(f'The spotify request could not be made because of the following error: {error_message}')