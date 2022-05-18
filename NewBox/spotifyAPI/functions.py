from authorization import spotifyHandler
from secrets import DEVICE_ID

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

    for i in range(0, resultSize):
        songInfo = {}
        songId = search[returnType + 's']['items'][i]['id']
        songName = search[returnType + 's']['items'][i]['name']
        uri = search[returnType + 's']['items'][i]['uri']
        # artistName = search[returnType + 's']['items'][i]['artists'][0]['name']

        songInfo.update({'nr': i + 1, 'type': returnType, 'songId': songId, 'songName': songName, 'uri': uri})
        items.append(songInfo)

    for i in range(len(items)):
        print(items[i])
    return items


def selectFromSearch(items):
    for i in range(len(items)):
        for j in items[i]:
            if items[i].get(j) == choice:
                play(items[i].get('uri'))



# Playlist related functions
def makePlaylist(userId, name, description=''):
    spotifyHandler.user_playlist_create(user=userId, name=name, description=description)


# def getPlaylistId():


def addSongsToPlaylist():
    spotifyHandler.playlist_add_items()


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
    # functie geeft nog error
    try:
        spotifyHandler.previous_track(device_id=DEVICE_ID)
    except spotipy.exceptions.SpotifyException as e:
        return


# set volume between 0 - 100%
def setVolume(volume):
    spotifyHandler.volume(device_id=DEVICE_ID, volume_percent=volume)

# inp = input("Search for a song, playlist, album etc: ")
# searchResult = searchFor(5, inp, returnType='playlist')
# choice = int(input("Enter number: "))
# selectFromSearch(searchResult)
# setVolume(0)
