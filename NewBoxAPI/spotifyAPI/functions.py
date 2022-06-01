import spotipy
from .secrets import DEVICE_ID, USER
from .authorization import spotifyHandler
import json


# User related functions
def getUserDetails():
    userId = spotifyHandler.me()['id']
    userUri = spotifyHandler.me()['uri']
    return userId, userUri


# Song related functions
def getPlaybackInfo():
    if spotifyHandler.current_playback() is None:
        return

    result = spotifyHandler.current_playback()

    track = result['item']['name']
    artist = result['item']['artists'][0]['name']
    volume = result['device']['volume_percent']
    repeatState = result['repeat_state']
    shuffleState = result['shuffle_state']
    isPlaying = result['is_playing']

    info = [{'track': track, 'artist': artist, 'volume': volume, 'repeatState': repeatState, 'shuffleState': shuffleState, 'isPlaying': isPlaying}]

    jsonObject = json.dumps(info)
    return jsonObject


def getSongById(trackId):
    track = spotifyHandler.track(trackId, market="NL")['name']
    return track


def getSongUri(trackName):
    return spotifyHandler.search(trackName, type='track')['tracks']['items'][0]['uri']


# Search related functions
def searchFor(resultSize, searchQuery, returnType='tracks'):
    items = []
    search = spotifyHandler.search(searchQuery, type=returnType)

    # Loop over all the search results and store each item with info to a dictionary and add the dict to a list
    for i in range(0, resultSize):
        itemInfo = {}
        id = search[returnType + 's']['items'][i]['id']
        name = search[returnType + 's']['items'][i]['name']
        uri = search[returnType + 's']['items'][i]['uri']

        itemInfo.update({'nr': i + 1,
                         'type': returnType,
                         'id': id,
                         'name': name,
                         'uri': uri})
        items.append(itemInfo)

    # Print out all the items
    for i in range(len(items)):
        print(items[i])
    jsonObject = json.dumps(items)
    return jsonObject


def selectFromSearch(items, inp):
    # Loop over all the items we got from SearchFor() function, if the number is what the user chose -> return the uri
    items = json.loads(items)
    for count, item in enumerate(items):
        if item.get('nr') == inp:
            return item.get('uri')


# Playlist related functions
def makePlaylist(name, description=''):
    spotifyHandler.user_playlist_create(user=USER, name=name, description=description)


def getPlaylistId(inp):
    items = searchFor(5, inp, returnType='playlist')
    select = int(input("Select playlist: "))
    return selectFromSearch(items, select)


def addSongToPlaylist(trackUri, playlistId):
    try:
        spotifyHandler.playlist_add_items(playlistId, [trackUri])
    except spotipy.SpotifyException:
        return -1


def removeSongsFromPlaylist(trackUri, playlistId):
    try:
        spotifyHandler.playlist_remove_all_occurrences_of_items(playlistId, [trackUri])
    except spotipy.SpotifyException:
        return -1


def getOwnPlaylists():
    playlists = []
    for count, playlist in enumerate(spotifyHandler.current_user_playlists()['items']):
        pl = {}
        uri = playlist['uri']
        name = playlist['name']
        id = playlist['id']

        pl.update({"nr": count + 1,
                   "name": name,
                   "uri": uri,
                   "id": id})

        playlists.append(pl)
    jsonObject = json.dumps(playlists)
    return jsonObject


def getPlaylistItems(playlistId):
    tracks = []
    playlist = spotifyHandler.playlist_items(playlist_id=playlistId, market='NL')['items']
    for count, songs in enumerate(playlist):
        track = {}
        artist = songs['track']['artists'][0]['name']
        trackName = songs['track']['name']
        duration = round(songs['track']['duration_ms'] / 60000, 2)

        track.update({"artist": artist,
                      "track": trackName,
                      "duration": duration})

        tracks.append(track)
    jsonObject = json.dumps(tracks)
    return jsonObject


def removePlaylist(playlistId):
    followedPlaylists = json.loads(getOwnPlaylists())
    for playlist in followedPlaylists:
        if playlist.get('id') == playlistId:
            spotifyHandler.current_user_unfollow_playlist(playlistId)
            return
    return -1


def getPlaylistCoverImage(playlistName):
    result = spotifyHandler.search(q=playlistName, limit=1, type='playlist')
    playlistId = result['playlists']['items'][0]['id']
    imageUrl = spotifyHandler.playlist_cover_image(playlistId)[0]['url']
    return imageUrl


def getTrackCoverImage(trackName):
    result = spotifyHandler.search(q=trackName, limit=1, type='track')
    trackId = result['tracks']['items'][0]['id']
    imageUrl = spotifyHandler.track(trackId)['album']['images'][0]['url']
    return imageUrl


def getDefaultPlaylists(limit):
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

    jsonObject = json.dumps(playlists)
    return jsonObject


# Player related functions
def play(uri):
    if 'track' in uri:
        uris = [uri]
        spotifyHandler.start_playback(device_id=DEVICE_ID, uris=uris)
    else:
        spotifyHandler.start_playback(device_id=DEVICE_ID, context_uri=uri)


def skip():
    spotifyHandler.next_track(device_id=DEVICE_ID)


def pause():
    if spotifyHandler.current_playback()['is_playing'] is True:
        spotifyHandler.pause_playback(device_id=DEVICE_ID)


def resume():
    if spotifyHandler.current_playback() is False:
        spotifyHandler.start_playback(device_id=DEVICE_ID)


def previous():
    lastTrackUri = spotifyHandler.current_user_recently_played(limit=1)['items'][0]['track']['uri']
    play(lastTrackUri)


def setVolume(volume):
    # set volume between 0 - 100%
    spotifyHandler.volume(device_id=DEVICE_ID, volume_percent=volume)


def shuffle():
    # state can either be true or false
    if not spotifyHandler.current_playback()['shuffle_state']:
        spotifyHandler.shuffle(device_id=DEVICE_ID, state=True)
    else:
        spotifyHandler.shuffle(device_id=DEVICE_ID, state=False)


def addToQueue(uri):
    if 'track' in uri:
        spotifyHandler.add_to_queue(device_id=DEVICE_ID, uri=uri)
    else:
        return -1


def repeat():
    # state can either be track, context or off
    if spotifyHandler.current_playback()['repeat_state'] == 'off':
        spotifyHandler.repeat(device_id=DEVICE_ID, state='track')
    else:
        spotifyHandler.repeat(device_id=DEVICE_ID, state='off')


def getFeaturedAlbums(limit):
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

    jsonObject = json.dumps(albums)
    return jsonObject
