from authorization import spotifyHandler


def getPlaybackState():

    if(spotifyHandler.current_playback() == None):
        print("No song currently playing")
        return

    result = spotifyHandler.current_playback()
    title = result['item']['name']

    print("'{}' is currently playing".format(title))


def getTrackById():
    print(spotifyHandler.track('2RChe0r2cMoyOvuKobZy44')['name'])


def searchForSong(searchLength):
    inp = input("Search for a song: ")
    search = spotifyHandler.search(inp)

    for i in range(0, searchLength):
        songId = search['tracks']['items'][i]['id']
        songName = search['tracks']['items'][i]['name']
        artistName = search['tracks']['items'][i]['artists'][0]['name']
        uri = search['tracks']['items'][i]['uri']
        print("{}. uri: {} song id: {}, song name: {}, artist name: {}".format(i + 1, uri, songId, songName, artistName))


def playSong():
    deviceId = spotifyHandler.devices()['devices'][0]['id']
    uri = ['spotify:track:53AddGhMgfIE85Az2Ipovu']
    spotifyHandler.start_playback(device_id=deviceId, uris=uri)


# getPlaybackState()
searchForSong(5)
# playSong()
