from SpotipyPlayer import SpotipyPlayer
spotipy_player = SpotipyPlayer()

try:
    context_uri = 'spotify:playlist:74sUjcvpGfdOvCHvgzNEDO'
    spotipy_player.play(context_uri, repeat=True, shuffle=True)
except Exception as error_message:
    print(f'The spotify request could not be made because of the following error: {error_message}')