from functools import wraps

import requests.exceptions
import spotipy
from .authorization import spotifyHandler
from .secrets import USER
import math

try:
    DEVICE_ID = spotifyHandler.devices()['devices'][0]['id']
except requests.exceptions.ConnectionError:
    DEVICE_ID = None
except IndexError:
    DEVICE_ID = None


# 'Decorator' that takes in a function as argument and checks if the function gives an error
def handle_connection(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            return {'status': 'error',
                    'message': 'ConnectionError, no internet'}
        except requests.exceptions.ReadTimeout:
            return {'status': 'error',
                    'message': 'ReadTimeOut, could not send request'}
    return decorated


# User related functions
@handle_connection
def getUserDetails():
    userId = spotifyHandler.me()['id']
    userUri = spotifyHandler.me()['uri']

    info = {'id': userId,
            'uri': userUri}
    return info


@handle_connection
def getDevice():
    try:
        return spotifyHandler.devices()['devices'][0]['id']
    except IndexError:
        return None
    except requests.exceptions.ConnectionError:
        return None


# Song related functions
@handle_connection
def getPlaybackInfo():
    result = spotifyHandler.current_playback()
    if result is None:
        return {'status': 'error',
                'message': 'No song playing'}

    track = result['item']['name']
    artist = result['item']['artists'][0]['name']
    uri = result['item']['uri']
    id = result['item']['id']
    volume = result['device']['volume_percent']
    repeatState = result['repeat_state']
    shuffleState = result['shuffle_state']
    isPlaying = result['is_playing']
    artistId = result['item']['artists'][0]['id']

    progressMinutes = math.floor(result['progress_ms'] / 60000)
    progressSeconds = math.floor((result['progress_ms'] / 1000) % 60)
    progress = f"{progressMinutes}.{progressSeconds}"

    progressSecondsAbsolute = math.floor(result['progress_ms'] / 1000)
    durationSecondsAbsolute = math.floor(result['item']['duration_ms'] / 1000)

    durationMinutes = math.floor(result['item']['duration_ms'] / 60000)
    durationSeconds = math.floor((result['item']['duration_ms'] / 1000) % 60)
    duration = f"{durationMinutes}.{durationSeconds}"

    coverImage = result['item']['album']['images'][0]['url']

    try:
        genre = spotifyHandler.artist(artistId)['genres'][0]
    except IndexError:
        genre = "None"

    info = {'track': track,
            'artist': artist,
            'uri': uri,
            'id': id,
            'volume': volume,
            'repeatState': repeatState,
            'shuffleState': shuffleState,
            'isPlaying': isPlaying,
            'progress': progress,
            'progress_seconds': progressSecondsAbsolute,
            'duration': duration,
            'duration_seconds': durationSecondsAbsolute,
            'img': coverImage,
            'genre': genre}

    return info


@handle_connection
def getSongByUri(trackUri):
    try:
        track = spotifyHandler.track(trackUri)['name']
        artist = spotifyHandler.track(trackUri)['artists'][0]['name']
    except spotipy.SpotifyException:
        info = {'status': 'error',
                'message': 'Invalid id'}
        return info

    info = {'name': track,
            'artist': artist}
    return info


@handle_connection
def getSongUri(trackName):
    try:
        uri = spotifyHandler.search(trackName, type='track')['tracks']['items'][0]['uri']
    except IndexError:
        info = {'status': 'error',
                'message': 'Invalid name'}
        return info

    uri = {'uri': uri}
    return uri


@handle_connection
def getSongDuration(uri):
    duration = round(spotifyHandler.track(uri)['duration_ms'] / 1000)
    return duration


# Search related functions
@handle_connection
def searchFor(resultSize, searchQuery, returnType='track'):
    # Check if result size is valid
    if resultSize <= 0 or resultSize > 50 or not isinstance(resultSize, int):
        return {'status': 'error', 'message': 'Invalid result size'}

    items = []
    searchResult = spotifyHandler.search(q=searchQuery, type=returnType, limit=resultSize)[returnType + 's']['items']

    # Loop over all the search results and store each item with info to a dictionary and add the dict to a list
    if returnType == "track":
        for count, item in enumerate(searchResult):
            # return item
            itemInfo = {}

            id = item['artists'][0]['id']
            name = item['name']
            artist = item['artists'][0]['name']
            uri = item['uri']

            itemInfo.update({'nr': count + 1,
                             'type': returnType,
                             'id': id,
                             'artist': artist,
                             'track': name,
                             'uri': uri})
            items.append(itemInfo)
    elif returnType == 'artist':
        for count, item in enumerate(searchResult):
            itemInfo = {}

            id = item['id']
            artist = item['name']
            uri = item['uri']

            itemInfo.update({'nr': count + 1,
                             'type': returnType,
                             'id': id,
                             'artist': artist,
                             'uri': uri})
            items.append(itemInfo)

    if not items:
        # if items is empty, return this
        return {'status': 'No results found'}

    return items


# Playlist related functions
@handle_connection
def makePlaylist(name, description=''):
    if spotifyHandler.user_playlist_create(user=USER, name=name, description=description):
        info = {'status': 'executed',
                'message': 'Created playlist'}
    else:
        info = {'status': 'error',
                'message': 'Could not create playlist'}
    return info


@handle_connection
def getPlaylistByName(inp):
    try:
        items = searchFor(1, inp, returnType='playlist')
    except IndexError:
        return {'status': 'error',
                'message': 'Could not find playlist'}
    return items


@handle_connection
def addSongToPlaylist(trackUri, playlistId):
    try:
        spotifyHandler.playlist_add_items(playlistId, [trackUri])
        info = {'status': 'executed',
                'message': 'Added song to playlist'}
    except spotipy.SpotifyException:
        info = {'status': 'error',
                'message': 'Could not add song to playlist'}
    return info


@handle_connection
def removeSongFromPlaylist(trackUri, playlistId):
    try:
        spotifyHandler.playlist_remove_all_occurrences_of_items(playlistId, [trackUri])
        info = {'status': 'executed',
                'message': 'Removed song from playlist'}
    except spotipy.SpotifyException:
        info = {'status': 'error',
                'message': 'Failed to remove song'}
    return info


@handle_connection
def getOwnPlaylists():
    playlists = []

    for count, playlist in enumerate(spotifyHandler.current_user_playlists()['items']):
        pl = {}
        try:
            img = playlist['images'][0]['url']
        except IndexError:
            img = "None"

        uri = playlist['uri']
        name = playlist['name']
        id = playlist['id']
        pl.update({"nr": count + 1,
                   "name": name,
                   "uri": uri,
                   "id": id,
                   "img": img})

        playlists.append(pl)

    if not playlists:
        info = {'status': 'executed',
                'message': 'No playlists'}
        return info

    return playlists


@handle_connection
def getTotal(id, returnType):
    # returnType can either be album or playlist
    try:
        if returnType == "playlist":
            total = spotifyHandler.playlist(id)['tracks']['total']
        elif returnType == "album":
            total = spotifyHandler.album(id)['total_tracks']
        else:
            total = {'status': 'error',
                     'message': 'Invalid returnType'}
        return total
    except spotipy.SpotifyException:
        info = {'status': 'error',
                'message': 'invalid id'}
        return info


@handle_connection
def getPlaylistItems(playlistId, offset=0, limit=100):
    tracks = []
    total = getTotal(id=playlistId, returnType="playlist")
    # Function above 'getPlaylistTotal' returns a dict if an error occurred.
    if isinstance(total, dict):
        return total

    for i in range(0, total, 100):
        playlist = spotifyHandler.playlist_items(playlist_id=playlistId, market='NL', offset=offset, limit=limit)
        offset += 100

        for count, songs in enumerate(playlist['items']):
            track = {}
            artist = songs['track']['artists'][0]['name']
            trackName = songs['track']['name']
            id = songs['track']['id']
            uri = songs['track']['uri']
            img = songs['track']['album']['images'][0]['url']
            durationMinutes = math.floor(songs['track']['duration_ms'] / 60000)
            durationSeconds = math.floor((songs['track']['duration_ms'] / 1000) % 60)
            duration = f"{durationMinutes}.{durationSeconds}"

            track.update({"artist": artist,
                          "track": trackName,
                          "duration": duration,
                          "uri": uri,
                          "id": id,
                          "img": img,
                          "total": total,
                          "nr": count + 1})

            tracks.append(track)

    if not tracks:
        info = {'status': 'executed',
                'message': 'Playlist is empty'}
        return info

    return tracks


@handle_connection
def removePlaylist(playlistId):
    followedPlaylists = getOwnPlaylists()
    # loop over all user playlists, if id matches -> remove playlist
    for playlist in followedPlaylists:
        if playlist.get('id') == playlistId:
            spotifyHandler.current_user_unfollow_playlist(playlistId)
            info = {'status': 'executed'}
            return info

    info = {'status': 'error',
            'message': 'Could not remove playlist, check if id is valid'}
    return info


@handle_connection
def getPlaylistCoverImage(playlistName):
    try:
        result = spotifyHandler.search(q=playlistName, limit=1, type='playlist')
        playlistId = result['playlists']['items'][0]['id']
    except IndexError:
        info = {'status': 'error',
                'message': 'Index out of range, no results found'}
        return info

    imageUrl = spotifyHandler.playlist_cover_image(playlistId)[0]['url']

    info = {'id': playlistId,
            'img': imageUrl}
    return info


@handle_connection
def getTrackCoverImage(trackName):
    try:
        result = spotifyHandler.search(q=trackName, limit=1, type='track')
        trackId = result['tracks']['items'][0]['id']
    except IndexError:
        info = {'status': 'error',
                'message': 'Index out of range, no results found'}
        return info

    imageUrl = spotifyHandler.track(trackId)['album']['images'][0]['url']

    info = {'id': trackId,
            'img': imageUrl}
    return info


@handle_connection
def getDefaultPlaylists(limit=20):
    # gets standard playlists to show on the front-end

    playlists = []
    result = spotifyHandler.featured_playlists(limit=limit)
    items = result['playlists']['items']
    for count, item in enumerate(items):
        playlist = {}
        name = item['name']
        id = item['id']
        uri = item['uri']
        description = item['description']
        img = item['images'][0]['url']
        playlist.update({"name": name,
                         "id": id,
                         "uri": uri,
                         "description": description,
                         "img": img})
        playlists.append(playlist)

    return playlists


# Player related functions
@handle_connection
def play(uri):
    if DEVICE_ID is None:
        return {'status': 'error',
                'message': 'No device found'}
    try:
        if 'track' in uri:
            uris = [uri]
            spotifyHandler.start_playback(device_id=DEVICE_ID, uris=uris)
        else:
            spotifyHandler.start_playback(device_id=DEVICE_ID, context_uri=uri)

        info = {'status': 'executed'}
        return info
    except spotipy.SpotifyException:
        info = {'status': 'error',
                'message': 'Invalid uri'}
        return info


@handle_connection
def skip():
    if spotifyHandler.current_playback()['item'] is None:
        info = {'status': 'No song available'}
        return info

    spotifyHandler.next_track(device_id=DEVICE_ID)
    spotifyHandler.repeat(device_id=DEVICE_ID, state='off')
    info = {'status': 'executed'}
    return info


@handle_connection
def pause():
    if spotifyHandler.current_playback() is None:
        return None
    if spotifyHandler.current_playback()['is_playing'] is True:
        spotifyHandler.pause_playback(device_id=DEVICE_ID)
    else:
        spotifyHandler.start_playback(device_id=DEVICE_ID)

    info = {'status': 'executed'}
    return info


@handle_connection
def previous():
    lastTrackUri = spotifyHandler.current_user_recently_played(limit=1)['items'][0]['track']['uri']
    play(lastTrackUri)
    info = {'status': 'executed'}
    return info


@handle_connection
def setVolume(volume):
    # set volume between 0 - 100%
    if not isinstance(volume, int) and not isinstance(volume, float):
        info = {'status': 'error',
                'message': 'Volume must be of type int or float'}
        return info

    if volume > 100:
        volume = 100

    if volume < 0:
        volume = 0

    volume = round(volume)
    spotifyHandler.volume(device_id=DEVICE_ID, volume_percent=volume)

    info = {'status': 'executed'}
    return info


@handle_connection
def shuffle():
    # state can either be true or false
    if spotifyHandler.current_playback() is None:
        info = {'status': 'No song available'}
        return info

    if not spotifyHandler.current_playback()['shuffle_state']:
        spotifyHandler.shuffle(device_id=DEVICE_ID, state=True)
    else:
        spotifyHandler.shuffle(device_id=DEVICE_ID, state=False)

    info = {'status': 'executed'}
    return info


@handle_connection
def addToQueue(uri):
    if 'track' in uri:
        try:
            spotifyHandler.add_to_queue(device_id=DEVICE_ID, uri=uri)
            info = {'status': 'executed',
                    'message': 'Added track to queue'}
        except spotipy.SpotifyException:
            info = {'status': 'error',
                    'message': 'Invalid track uri'}
    else:
        info = {'status': 'error',
                'message': 'Can only add songs to queue'}
    return info


@handle_connection
def repeat():
    # state can either be track, context or off
    if spotifyHandler.current_playback() is None:
        info = {'status': 'No song available'}
        return info

    if spotifyHandler.current_playback()['repeat_state'] == 'off':
        spotifyHandler.repeat(device_id=DEVICE_ID, state='track')
    else:
        spotifyHandler.repeat(device_id=DEVICE_ID, state='off')

    info = {'status': 'executed'}
    return info


@handle_connection
def getFeaturedAlbums(limit=20):
    albums = []
    items = spotifyHandler.new_releases(limit=limit)['albums']['items']
    for count, item in enumerate(items):
        album = {}
        name = item['name']
        id = item['id']
        uri = item['uri']
        img = item['images'][0]['url']

        album.update({"name": name,
                      "id": id,
                      "uri": uri,
                      "img": img})
        albums.append(album)

    return albums


@handle_connection
def getCategories(limit=50):
    categories = []
    items = spotifyHandler.categories(limit=limit)['categories']['items']
    for count, item in enumerate(items):
        category = {}
        name = item['name']
        id = item['id']
        category.update({'name': name,
                         'id': id})
        categories.append(category)

    return categories


@handle_connection
def getTopArtists(limit=20):
    artists = []
    items = spotifyHandler.current_user_top_artists(limit=limit)['items']
    for count, item in enumerate(items):
        artist = {}
        name = item['name']
        id = item['id']
        popularity = item['popularity']
        img = item['images'][0]['url']
        uri = item['uri']
        artist.update({'name': name,
                       'id': id,
                       'popularity': popularity,
                       'img': img,
                       'uri': uri})
        artists.append(artist)
    return artists


@handle_connection
def getTopTracks(limit=20):
    tracks = []
    items = spotifyHandler.current_user_top_tracks(limit=limit)['items']
    for count, item in enumerate(items):
        track = {}
        name = item['name']
        id = item['id']
        uri = item['uri']
        img = item['album']['images'][0]['url']
        track.update({'name': name,
                      'id': id,
                      'uri': uri,
                      'img': img})
        tracks.append(track)

    return tracks


@handle_connection
def getAlbumItems(albumId, offset=0, limit=50):
    tracks = []
    total = getTotal(id=albumId, returnType="album")
    # Function above 'getPlaylistTotal' returns a dict if an error occurred.
    if isinstance(total, dict):
        return total

    for i in range(0, total, 100):
        album = spotifyHandler.album_tracks(album_id=albumId, market='NL', offset=offset, limit=limit)
        offset += 100
        for count, songs in enumerate(album['items']):
            track = {}
            artist = songs['artists'][0]['name']
            trackName = songs['name']
            id = songs['id']
            uri = songs['uri']
            # img = songs['track']['album']['images'][0]['url']
            durationMinutes = math.floor(songs['duration_ms'] / 60000)
            durationSeconds = math.floor((songs['duration_ms'] / 1000) % 60)
            duration = f"{durationMinutes}.{durationSeconds}"

            track.update({"artist": artist,
                          "track": trackName,
                          "duration": duration,
                          "uri": uri,
                          "id": id,
                          "total": total,
                          "nr": count + 1})

            tracks.append(track)
    return tracks


@handle_connection
def getTopSongsByArtist(artistId):
    tracks = []
    items = spotifyHandler.artist_top_tracks(artistId)["tracks"]
    for count, item in enumerate(items):
        track = {}
        name = item['name']
        id = item['id']
        uri = item['uri']
        img = item['album']['images'][0]['url']
        track.update({'track': name,
                      'id': id,
                      'uri': uri,
                      'img': img})
        tracks.append(track)

    return tracks
