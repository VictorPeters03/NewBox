from authorization import spotifyHandler


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
    songs = []
    search = spotifyHandler.search(searchQuery, type=returnType)

    for i in range(0, resultSize):
        songInfo = {}
        songId = search[returnType + 's']['items'][i]['id']
        songName = search[returnType + 's']['items'][i]['name']
        uri = search[returnType + 's']['items'][i]['uri']
        # artistName = search[returnType + 's']['items'][i]['artists'][0]['name']

        songInfo.update({'nr': i + 1, 'type': returnType, 'songId': songId, 'songName': songName, 'uri': uri})
        songs.append(songInfo)

    for i in range(len(songs)):
        print(songs[i])
    return songs


def selectFromSearch(items):
    for i in range(len(items)):
        for j in items[i]:
            if items[i].get(j) == choice:
                play(items[i].get('uri'))


def play(uri):
    deviceId = spotifyHandler.devices()['devices'][0]['id']
    uris = [uri]
    spotifyHandler.start_playback(device_id=deviceId, uris=uris)


# Playlist related functions
def makePlaylist(userId, name, description=''):
    spotifyHandler.user_playlist_create(user=userId, name=name, description=description)


# def getPlaylistId():


def addSongsToPlaylist():
    spotifyHandler.playlist_add_items()


# inp = input("Search for a song: ")
# searchResult = searchFor(5, inp, returnType='playlist')
# choice = int(input("Enter number: "))
# selectFromSearch(searchResult)
