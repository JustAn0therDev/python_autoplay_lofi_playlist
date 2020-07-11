import SpotipyPlayer

spotipy_player = SpotipyPlayer()

try:
    spotipy_player.get_token()
    spotipy_player.initialize_spotipy_to_get_first_available_device()
    spotipy_player.start_playback()
    spotipy_player.repeat_playback()
    spotipy_player.shuffle_playback()
except Exception as error_message:
    print(f'The spotify request could not be made because of the following error: {error_message}')