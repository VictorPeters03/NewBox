
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


def searchForSongs(resultSize):
    songs = []
    inp = input("Search for a song: ")
    search = spotifyHandler.search(inp)

    for i in range(0, resultSize):
        dict = {}
        songId = search['tracks']['items'][i]['id']
        songName = search['tracks']['items'][i]['name']
        artistName = search['tracks']['items'][i]['artists'][0]['name']
        uri = search['tracks']['items'][i]['uri']

        dict.update({'nr': i + 1, 'songId': songId, 'songName': songName, 'artistName': artistName, 'uri': uri})
        songs.append(dict)


    for i in range(len(songs)):
        print(songs[i])

    choice = int(input("Enter number: "))

    for i in range(len(songs)):
        for j in songs[i]:
            # print(songs[i].get(j))
            if(songs[i].get(j) == choice):
                playSong(songs[i].get('uri'))


def playSong(uri):
    deviceId = spotifyHandler.devices()['devices'][0]['id']
    uris = [uri]
    spotifyHandler.start_playback(device_id=deviceId, uris=uris)

# getPlaybackState()
searchForSongs(5)
# playSong()
