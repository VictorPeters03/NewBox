import MySQLdb
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socket
import json
from spotifyAPI import functions
import os
from time import sleep
import vlc
import asyncio
import player
# import alsaaudio



app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


queue = []

def get_volume_limits():
    f = open('max.txt', 'r')
    max_volume = int(f.read())
    f.close()
    
    f = open('min.txt', 'r')
    min_volume = int(f.read())
    f.close()
    return min_volume, max_volume

def set_volume_limit(amount : int, limit : str):
    if limit == 'min':
        f = open('min.txt', 'r')
        volume_limit = int(f.read())
        f.close()
        return volume_limit
    elif limit == 'max':
        f = open('max.txt', 'r')
        volume_limit = int(f.read())
        f.close()
        return volume_limit
    return volume_limit


# http://larsimmisch.github.io/pyalsaaudio/libalsaaudio.html#module-alsaaudio
# endpoint for setting the volume
@app.put("/adminpanel/volume/{amount}")
async def set_volume(amount: int):
    valid = False
    limits = get_volume_limits()
    while not valid:
        try:
            if (amount <= limits[1]) and (amount >= limits[0]):
                # mixer = alsaaudio.Mixer('PCM')
                # mixer.setvolume(amount)
                volume = json.dumps({"volume": amount})
                valid = True
            elif amount > limits[1]:
                volume = json.dumps({"volume": limits[1],
                                     "mess": "Input volume was higher than the maximum volume. Volume is set to the maximum volume."})
                valid = True
            elif amount < limits[0]:
                volume = json.dumps({"volume": limits[0],
                                     "mess": "Input volume was lower than the minimum volume. Volume is set to the minimum volume."})
                valid = True
        except ValueError:
            valid = False
    return volume


# endpoint for setting the maximum volume
@app.put("/adminpanel/maxvolume/{amount}")
async def set_max_volume(amount: int):
    limits = get_volume_limits()
    if (amount <= 100) and (amount >= 0) and (amount > limits[0]):
        set_volume_limit(amount, 'max')
        max_volume = amount
        mess = "Maximum volume is set to" + str(max_volume) + "."
    elif amount < limits[0]:
        mess = "Maximum volume is lower than the minimum volume. That is not possible."
        max_volume = limits[1]
    else:
        mess = "Maximum volume is not in the range of 0-100."
        max_volume = limits[1]
    return json.dumps({"mess": mess, "max_volume": max_volume})


# endpoint for setting the minimum volume
@app.put("/adminpanel/minvolume/{amount}")
async def set_min_volume(amount: int):
    limits = get_volume_limits()
    if (amount <= 100) and (amount >= 0) and (limits[1] > amount):
        set_volume_limit(amount, 'min')
        min_volume = amount
        mess = "Minimum volume is set to" + str(min_volume) + "."
    elif limits[1] < amount:
        min_volume = limits[0]
        mess = "Minimum volume is higher than the maximum volume. That is not possible."
    else:
        min_volume = limits[0]
        mess = "Minimum volume is not in the range of 0-100."
    return json.dumps({"mess": mess, "min_volume": min_volume})


# endpoint for adding a song to the queue
@app.put("/use/queue/{uri}")
def add_to_queue(uri: str):
    player.addToQueue(uri)


# endpoint for getting the queue
@app.get("/use/getQueue")
async def get_queue():
    return player.getQueue()


# endpoint for playing songs
@app.get("/use/getsongs")
async def get_songs():
    # needs an if statement added to check if the queue is empty

    # sets up a connection to the database
    try:
        db = MySQLdb.connect("127.0.0.1", "root", "", "djangosearchbartest")
    except:
        return "Can't connect to database"

    cursor = db.cursor()

    # the SQL statement
    sql = "SELECT * FROM `core_song` ORDER BY `artist`;"
    # song_id = id
    #  WHERE id = %s
    # executes the statement
    cursor.execute(sql)
    # , song_id
    # takes the data from the statement and places it in a variable
    songs = cursor.fetchall()

    db.close()

    dictionary = []

    for song in songs:
        dictionary.append({"id": song[0], "artist": song[1], "track": song[2], "uri": song[3]})

    return dictionary


# endpoint for searching individual songs in the local database
@app.get("/use/search/{key}")
async def search_music(key: str):
    # sets up a connection to the database
    try:
        db = MySQLdb.connect("127.0.0.1", "root", "", "djangosearchbartest")
    except:
        return "Can't connect to database"

    cursor = db.cursor()

    # the SQL statement
    sqlSongs = "SELECT * FROM `core_song` WHERE `song` LIKE %s;"
    sqlArtists = "SELECT * FROM `core_song` WHERE `artist` LIKE %s;"

    params = [key + "%"]

    # executes the statement
    cursor.execute(sqlSongs, params)
    # , song_id
    # takes the data from the statement and places it in a variable
    songs = cursor.fetchall()

    dictionary = []

    for song in songs:
        dictionary.append({"type": "downloaded", "id": song[0], "artist": song[1], "track": song[2], "uri": song[3]})

    cursor.execute(sqlArtists, params)

    songs = cursor.fetchall()

    for song in songs:
        dictionary.append({"type": "downloaded", "id": song[0], "artist": song[1], "track": song[2], "uri": song[3]})

    artistsSpotify = functions.searchFor(2, key, 'artist')

    for artist in artistsSpotify:
        dictionary.append({"type": artist["type"], "id": artist['id'], "artist": artist['artist'], "uri": artist['uri']})

    songsSpotify = functions.searchFor(10, key)

    for song in songsSpotify:
        dictionary.append({"type": song["type"], "id": song['id'], "artist": song['artist'], "track": song['track'], "uri": song['uri']})

    return dictionary
    # return artistsSpotify

# endpoint for getting all songs
@app.get("use/searchall/{key}")
async def search_all(key: str):
    # sets up a connection to the database
    try:
        db = MySQLdb.connect("127.0.0.1", "root", "", "djangosearchbartest")
    except:
        return "Can't connect to database"

    cursor = db.cursor()

    # the SQL statement
    sql = "SELECT * FROM `core_song`;"

    # executes the statement
    cursor.execute(sql)

    # takes the data from the statement and places it in a variable
    songs = cursor.fetchall()

    db.close()

    dictionary = []

    for song in songs:
        dictionary.append({"id": song[0], "artist": song[1], "title": song[2]})

    return dictionary


# endpoint for getting the ip off the rpi
@app.get("/adminpanel/ip")
async def get_ip():
    return json.dumps({"ip": socket.gethostbyname(socket.gethostname())})


# SPOTIFY FUNCTIONS
@app.get("/use/userDetails")
async def getUserDetails():
    return functions.getUserDetails()


@app.get("/use/getPlaybackInfo")
async def getPlaybackInfo():
    return functions.getPlaybackInfo()


@app.put("/use/toggle")
async def toggle():
    player.toggle()


@app.get("/use/getDevice")
async def getDevice():
    return functions.getDevice()


@app.put("/use/skip")
async def skip():
    return player.skip()


@app.put("/use/playSong")
async def playSong():
    player.playSong()


@app.get("/use/getOwnPlaylists")
async def getOwnPlaylists():
    return functions.getOwnPlaylists()


@app.get("/use/getPlaylistItems/{id}")
async def getPlaylistItems(id):
    return functions.getPlaylistItems(id)


@app.get("/use/getAlbumItems/{id}")
async def getAlbumItems(id):
    return functions.getAlbumItems(id)


@app.get("/use/getFeaturedPlaylists")
async def getFeaturedPlaylists():
    return functions.getDefaultPlaylists()


@app.get("/use/getFeaturedAlbums")
async def getFeaturedAlbums():
    return functions.getFeaturedAlbums()


@app.post("/use/addSongToPlaylist/{trackUri}&{playlistId}")
async def addSongToPlaylist(trackUri, playlistId):
    return functions.addSongToPlaylist(trackUri, playlistId)


@app.delete("/use/removeSongFromPlaylist/{trackUri}&{playlistId}")
async def removeSongFromPlaylist(trackUri, playlistId):
    return functions.removeSongFromPlaylist(trackUri, playlistId)


@app.get("/use/searchInSpotify/{query}&{resultSize}")
async def searchInSpotify(query, resultSize):
    return functions.searchFor(query, int(resultSize))


@app.get("/use/getTopTracks")
async def getTopTracks():
    return functions.getTopTracks()


@app.get("/use/getTopArtists")
async def getTopArtists():
    return functions.getTopArtists()


@app.get("/use/getCategories")
async def getCategories():
    return functions.getCategories()