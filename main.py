import Spotipy_Player

spotipy_player = Spotipy_Player.Spotipy_Player()

try:
    spotipy_player.get_token()
    spotipy_player.initalize_spotipy()
    spotipy_player.get_first_available_device()
    spotipy_player.start_playback()
    spotipy_player.repeat_playback('context')
    spotipy_player.shuffle_playback(True)
except Exception as error_message:
    print(f'The spotify request could not be made because of the following error: {error_message}')