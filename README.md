# python_autoplay_lofi_playlist
A simple and small python project for playing any playlist, song or album on repeat or shuffle (configurable).

## Notes 

I made this project initially only to play a lofi playlist I like a lot, but it came to me that this project should be easily configurable, so now its easier to make the Spotify API play anything else only by changing one line of code, which will be passed as a parameter to the only public SpotipyPlayer class method in the main.py file.

The API integration was not as cool as I thought it was. The whole idea of automating Spotify to play a playlist as soon as I bootup my Windows PC needs a grant permission first, which is made by prompting the user for permission by clicking on a button. Luckily, there's a library called Spotipy that solves this issue. It's really good and pretty simple, you can find the documentation for it [here](https://spotipy.readthedocs.io/en/2.12.0/).

Please feel free to use the project as you see fit.

If your player of choice has a public API but it's not Spotify, you may not be able to use the script "as is", but the main logic for requesting to play a song while logged in to your account should be pretty much the same.

### Credentials

The credentials can follow the same way I made mine, with a few constants on a separate file, but it needs to be generated in the Spotify API dashboard!
