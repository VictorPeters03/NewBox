import spotipy
from authorization import spotifyHandler


def getArtistId(query):
    result = spotifyHandler.search(q=query, limit=1, type='artist')
    return result['artists']['items'][0]['id']


# Artist related functions
def getArtistByID(artistName):
    art = getArtistId(artistName)
    return spotifyHandler.artist(art)['uri']


def getAlbumByArtist(artist_id):
    return spotifyHandler.artist_albums(artist_id)


# Album related functions
def getAlbumByID(album_id):
    return spotifyHandler.album(album_id)


def getAlbumTracks(album_id):
    return spotifyHandler.album_tracks(album_id)


# Track related functions
def getTrackId(query):
    result = spotifyHandler.search(q=query, limit=1, type='track')
    return result['tracks']['items'][0]['id']


def getTrackByID(trackName):
    track = getTrackId(trackName)
    return spotifyHandler.track(track)['uri']

