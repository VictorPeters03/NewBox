import spotipy
from authorization import spotifyHandler
from secrets import DEVICE_ID, USER


# GetID function (is also in 'functions' so should be removed)
def getArtistId(query):
    result = spotifyHandler.search(q=query, limit=1, type='artist')
    return result['artists']['items'][0]['id']


# Artist related functions
def getArtistByID(artistName):
    art = getArtistId(artistName)
    print(spotifyHandler.artist(art)['uri'])


def getAlbumByArtist(artist_id):
    print(spotifyHandler.artist_albums(artist_id))


# Album related functions
def getAlbumByID(album_id):
    print(spotifyHandler.album(album_id)['name']['uri'])


def getAlbumTracks(album_id):
    print(spotifyHandler.album_tracks(album_id))


# Track related functions
def getTrackId(query):
    result = spotifyHandler.search(q=query, limit=1, type='track')
    return result['tracks']['items'][0]['id']


def getTrackByID(trackName):
    track = getTrackId(trackName)
    print(spotifyHandler.track(track)['uri'])


getTrackByID('Satellite Mind')