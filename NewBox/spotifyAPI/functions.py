from authorization import spotifyHandler


# User related functions
def getUserDetails():
    userId = spotifyHandler.me()['id']
    userUri = spotifyHandler.me()['uri']
    print(userId)


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


def searchForSongs(resultSize, searchQuery):
    songs = []
    search = spotifyHandler.search(searchQuery)

    for i in range(0, resultSize):
        songInfo = {}
        songId = search['tracks']['items'][i]['id']
        songName = search['tracks']['items'][i]['name']
        artistName = search['tracks']['items'][i]['artists'][0]['name']
        uri = search['tracks']['items'][i]['uri']

        songInfo.update({'nr': i + 1, 'songId': songId, 'songName': songName, 'artistName': artistName, 'uri': uri})
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


def searchForPlaylist(resultSize, searchQuery):
    playlists = []
    search = spotifyHandler.search(searchQuery, type='playlist')

    for i in range(0, resultSize):
        playlistInfo = {}
        playlistUri = search['playlists']['items'][i]['uri']
        playlistId = search['playlists']['items'][i]['id']
        playlistName = search['playlists']['items'][i]['name']

        playlistInfo.update({'nr': i + 1, 'uri': playlistUri, 'playlistId': playlistId, 'playlistName': playlistName})
        playlists.append(playlistInfo)

    for i in range(len(playlists)):
        print(playlists[i])
    return playlists


# def getPlaylistId():


def addSongsToPlaylist():
    spotifyHandler.playlist_add_items()


# inp = input("Search for a song: ")
# searchResult = searchForPlaylist(5, inp)
# choice = int(input("Enter number: "))
# selectFromSearch(searchResult)
