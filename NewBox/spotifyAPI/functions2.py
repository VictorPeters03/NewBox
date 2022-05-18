import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import artist_IDs
from array import *
from authorization import spotifyHandler

# Albums van artiesten ophalen

artist_array = array('u', [artist_IDs.ed_sheeran, artist_IDs.drake, artist_IDs.bad_bunny, artist_IDs.the_weeknd,
                           artist_IDs.ariana_grande, artist_IDs.justin_bieber, artist_IDs.taylor_swift,
                           artist_IDs.eminem,
                           artist_IDs.post_malone, artist_IDs.BTS, artist_IDs.j_balvin, artist_IDs.kanye_west,
                           artist_IDs.juice_wrld, artist_IDs.coldplay, artist_IDs.xxxtentacion, artist_IDs.dua_lipa,
                           artist_IDs.ozuna, artist_IDs.imagine_dragons, artist_IDs.khalid, artist_IDs.travis_scott,
                           artist_IDs.rihanna, artist_IDs.marshmello, artist_IDs.maroon_5, artist_IDs.shawn_mendes,
                           artist_IDs.david_guetta, artist_IDs.bruno_mars, artist_IDs.daddy_yankee,
                           artist_IDs.calvin_harris, artist_IDs.sam_smith, artist_IDs.kendrick_lamar,
                           artist_IDs.queen,
                           artist_IDs.the_chainsmokers, artist_IDs.one_direction, artist_IDs.future,
                           artist_IDs.chris_brown, artist_IDs.beyonce, artist_IDs.nicki_minaj, artist_IDs.lady_gaga,
                           artist_IDs.j_cole, artist_IDs.anuel_aa, artist_IDs.halsey, artist_IDs.adele,
                           artist_IDs.selena_gomez, artist_IDs.the_beatles, artist_IDs.sia, artist_IDs.maluma,
                           artist_IDs.twenty_one_pilots, artist_IDs.marshmello, artist_IDs.lil_uzi_vert,
                           artist_IDs.linkin_park])

artist_chosen = artist_array[16]  # Placeholder voor een 'post' functie wanneer een artiest geselecteerd wordt.
artist_uri = 'spotify:artist:{}'.format(artist_chosen)
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_albums(artist_uri, album_type='album')
albums = results['items']

while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])