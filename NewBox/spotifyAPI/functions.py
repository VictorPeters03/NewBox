import spotipy
from authorization import spotifyHandler
from secrets import DEVICE_ID, USER


# User related functions
def getUserDetails():
    userId = spotifyHandler.me()['id']
    userUri = spotifyHandler.me()['uri']
    return userId, userUri


# Song related functions
def getPlaybackState():
    if spotifyHandler.current_playback() is None:
        print("No song currently playing")
        return

    result = spotifyHandler.current_playback()
    title = result['item']['name']

    print(f"'{title}' is currently playing")


def getSongById(songId):
    print(spotifyHandler.track(songId)['name'])


def searchFor(resultSize, searchQuery, returnType='tracks'):
    items = []
    search = spotifyHandler.search(searchQuery, type=returnType)

    # Add item info to a dictionary
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
    return items


def selectFromSearch(items, inp):
    for i in range(len(items)):
        for j in items[i]:
            if items[i].get(j) == inp:
                return items[i].get('uri')


# Playlist related functions
def makePlaylist(name, description=''):
    spotifyHandler.user_playlist_create(user=USER, name=name, description=description)


def getPlaylistId(inp):
    items = searchFor(5, inp, returnType='playlist')
    select = int(input("Select playlist: "))
    return selectFromSearch(items, select)


def addSongsToPlaylist():
    inp = input("Select playlist to add songs to: ")
    playlists = getOwnPlaylists()
    songs = searchFor(5, inp, returnType='track')
    choice = input("Choose an option: ")
    selected = selectFromSearch(songs, choice)
    for playlist in playlists:
        if playlist.get('name').lower() == inp.lower():
            playlistId = playlist.get('id')
            spotifyHandler.playlist_add_items(playlistId, selected)
    playlistId = getPlaylistId(inp)
    spotifyHandler.playlist_add_items(playlistId, inp)


def getOwnPlaylists():
    playlists = []
    for count, playlist in enumerate(spotifyHandler.current_user_playlists()['items']):
        pl = {}
        uri = playlist['uri']
        name = playlist['name']
        id = playlist['id']
        pl.update({"name": name, "uri": uri, "id": id})
        playlists.append(pl)
    print(playlists)
    return playlists


def removePlaylist():
    inp = input("Enter playlist name: ")
    playlists = getOwnPlaylists()
    for playlist in playlists:
        if playlist.get('name').lower() == inp.lower():
            spotifyHandler.current_user_unfollow_playlist(playlist.get('id'))
            return
    print("Could not find a playlist with that name")


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
    spotifyHandler.pause_playback(device_id=DEVICE_ID)


def resume():
    spotifyHandler.start_playback(device_id=DEVICE_ID)


def previous():
    # function gives an error, needs fix
    try:
        spotifyHandler.previous_track(device_id=DEVICE_ID)
    except spotipy.exceptions.SpotifyException:
        return


def setVolume(volume):
    # set volume between 0 - 100%
    spotifyHandler.volume(device_id=DEVICE_ID, volume_percent=volume)


def shuffle(state):
    # state can either be true or false
    spotifyHandler.shuffle(device_id=DEVICE_ID, state=state)


def addToQueue(uri):
    if 'track' in uri:
        spotifyHandler.add_to_queue(device_id=DEVICE_ID, uri=uri)
    else:
        print('cannot add playlist or album to queue')
        return


def setRepeat(state):
    # state can either be track, context or off
    spotifyHandler.repeat(state=state, device_id=DEVICE_ID)


# inp = input("Search for a song, playlist, album etc: ")
# searchResult = searchFor(5, inp, returnType='playlist')
# choice = int(input("Enter number: "))
# playThisUri = selectFromSearch(searchResult, choice)
# play(playThisUri)
# addSongsToPlaylist()