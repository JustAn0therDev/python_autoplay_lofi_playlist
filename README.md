# python_autoplay_lofi_playlist
A simple and small python project for playing any playlist, song or album on repeat or shuffle (configurable).

## Notes 

I made this project initially only to play a lofi playlist I like a lot, but it came to me that this project should as easily configurable as possible, so now its easier to make the Spotify API play anything else only by changing one line of code.

The API integration was not as cool as I thought it was. The whole idea of automating Spotify to play a playlist as soon as I bootup my Windows PC needs a grant permission first, which is made by prompting the user for permission by clicking on a button. Luckily, there's a library called Spotipy that solves this issue. It's really good and pretty simple, you can find the documentation for it [here](https://spotipy.readthedocs.io/en/2.12.0/).

Feel free to use the project as you like.

### Credentials

The credentials can follow the same way I made mine, with a few constants on a separate file, but it needs to be generated in the Spotify API dashboard!
