import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import artist_IDs
from array import *
import numpy as np


# from authorization import spotifyHandler

# Albums van artiesten ophalen

def get_album_by_artist():
    artist_array = np.array([artist_IDs])

    artist_chosen = artist_array[16]  # Placeholder voor een 'post' functie wanneer een artiest
    # geselecteerd wordt.
    artist_uri = 'spotify:artist:{}'.format(artist_chosen)
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.artist_albums(artist_uri, album_type='album')
    albums = results['items']

    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])

    return


get_album_by_artist()
