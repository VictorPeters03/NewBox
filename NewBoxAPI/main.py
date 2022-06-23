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
import alsaaudio
from colorthief import ColorThief
from colormap import hex2rgb
import serial
from urllib.request import urlretrieve
import urllib3

app = FastAPI()

# enable CORS middleware to work with axios requests
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
titleLimit = 40


def songExists(item):
    if "status" in item:
        return False
    return True


def itemCharLimitExceeded(item, artistKey, songKey):
    if len(item[artistKey]) <= titleLimit < len(item[songKey]):
        return 1
    elif len(item[artistKey]) > titleLimit and len(item[songKey]) > titleLimit:
        return 2
    elif len(item[artistKey]) > titleLimit >= len(item[songKey]):
        return 3
    else:
        return 4


# def appropriate():



# endpoint for getting volume limits
@app.get("/adminpanel/getlimits")
def get_volume_limits():
    f = open('max.txt', 'r')
    max_volume = int(f.read())
    f.close()

    f = open('min.txt', 'r')
    min_volume = int(f.read())
    f.close()
    return min_volume, max_volume

#endpoint for muting and unmuting volume 
@app.get("/adminpanel/togglemute")
def toggle_mute():
     os.popen("pactl set-sink-mute 0 toggle").read()

# endpoint for setting the minimum or maximum volume.
def set_volume_limit(amount: int, limit: str):
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
                mixer = alsaaudio.Mixer('Master')

                mixer.setvolume(amount)

                volume = json.dumps({"volume": amount})
                valid = True
            elif amount > limits[1]:
                volume = json.dumps({"volume": limits[1],
                                     "mess": "Input volume was higher than the maximum volume. Volume is set to the maximum volume."})
                mixer = alsaaudio.Mixer('Master')
                mixer.setvolume(limits[1])
                valid = True
            elif amount < limits[0]:
                volume = json.dumps({"volume": limits[0],
                                     "mess": "Input volume was lower than the minimum volume. Volume is set to the minimum volume."})
                mixer = alsaaudio.Mixer('Master')
                mixer.setvolume(limits[0])
                valid = True
        except ValueError:
            valid = False
    return volume

@app.put("/adminpanel/mute")
async def set_volume_mute():
    mixer = alsaaudio.Mixer('Master')
    mixer.setmute()
    return

@app.put("/adminpanel/harder")
async def set_volume_harder():
    mixer = alsaaudio.Mixer('Master')
    mixer.setvolume(mixer.getvolume(0)[1] + 5)

@app.put("/adminpanel/softer")
async def set_volume_softer():
    mixer = alsaaudio.Mixer('Master')
    mixer.setvolume(mixer.getvolume(0)[1] - 5)
    return 

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
    return player.addToQueue(uri)


# endpoint for getting the queue
@app.get("/use/getQueue")
def get_queue():
    try:
        return player.getQueue()
    except KeyError:
        player.filterQueue()
    finally:
        return player.getQueue()


# endpoint for playing songs
@app.get("/use/getsongs")
async def get_songs():
    # needs an if statement added to check if the queue is empty

    # sets up a connection to the database
    try:
        db = MySQLdb.connect("127.0.0.1", "newboxsql", "newbox", "songsdatabase")
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
        if itemCharLimitExceeded(song, 1, 2) == 1:
            dictionary.append({"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1],
                               "track": song[2][0:titleLimit] + "...", "uri": song[3]})
        elif itemCharLimitExceeded(song, 1, 2) == 2:
            dictionary.append(
                {"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1][0:titleLimit] + "...",
                 "track": song[2][0:titleLimit] + "...", "uri": song[3]})
        elif itemCharLimitExceeded(song, 1, 2) == 3:
            dictionary.append(
                {"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1][0:titleLimit] + "...",
                 "track": song[2],
                 "uri": song[3]})
        else:
            dictionary.append(
                {"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1], "track": song[2],
                 "uri": song[3]})

    return dictionary


# endpoint for searching individual songs and artists in the local database and spotify
@app.get("/use/search/{key}")
def search_music(key: str):
    # sets up a connection to the database
    try:
        db = MySQLdb.connect("127.0.0.1", "newboxsql", "newbox", "songsdatabase")
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
        if len(songs) == 0:
            break
        elif itemCharLimitExceeded(song, 1, 2) == 1:
            dictionary.append({"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1],
                               "track": song[2][0:titleLimit] + "...", "uri": song[3]})
        elif itemCharLimitExceeded(song, 1, 2) == 2:
            dictionary.append(
                {"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1][0:titleLimit] + "...",
                 "track": song[2][0:titleLimit] + "...", "uri": song[3]})
        elif itemCharLimitExceeded(song, 1, 2) == 3:
            dictionary.append(
                {"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1][0:titleLimit] + "...",
                 "track": song[2],
                 "uri": song[3]})
        else:
            dictionary.append(
                {"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1], "track": song[2],
                 "uri": song[3]})

    cursor.execute(sqlArtists, params)

    songs = cursor.fetchall()

    for song in songs:
        if len(songs) == 0:
            break
        if itemCharLimitExceeded(song, 1, 2) == 1:
            dictionary.append({"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1],
                               "track": song[2][0:titleLimit] + "...", "uri": song[3]})
        elif itemCharLimitExceeded(song, 1, 2) == 2:
            dictionary.append(
                {"type": "track", "isDownloaded": True, "id": song[0],
                 "artist": song[1][0:titleLimit] + "...",
                 "track": song[2][0:titleLimit] + "...", "uri": song[3]})
        elif itemCharLimitExceeded(song, 1, 2) == 3:
            dictionary.append(
                {"type": "track", "isDownloaded": True, "id": song[0],
                 "artist": song[1][0:titleLimit] + "...",
                 "track": song[2],
                 "uri": song[3]})
        else:
            dictionary.append(
                {"type": "track", "isDownloaded": True, "id": song[0], "artist": song[1],
                 "track": song[2],
                 "uri": song[3]})

    artistsSpotify = functions.searchFor(2, key, 'artist')

    for artist in artistsSpotify:
        if not songExists(artist):
            break
        elif len(artist["artist"]) > titleLimit:
            dictionary.append(
                {"type": artist["type"], "id": artist['id'], "artist": artist['artist'][0:titleLimit] + "...",
                 "uri": artist['uri']})
        else:
            dictionary.append(
                {"type": artist["type"], "id": artist["id"], "artist": artist["artist"], "uri": artist["uri"]})

    songsSpotify = functions.searchFor(10, key)

    for song in songsSpotify:
        if not songExists(song):
            break
        elif itemCharLimitExceeded(song, "artist", "track") == 1:
            dictionary.append({"type": song["type"], "isDownloaded": False, "id": song['id'], "artist": song['artist'],
                               "track": song['track'][0:titleLimit] + "...", "uri": song['uri']})
        elif itemCharLimitExceeded(song, "artist", "track") == 2:
            dictionary.append({"type": song["type"], "isDownloaded": False, "id": song['id'],
                               "artist": song['artist'][0:titleLimit] + "...",
                               "track": song['track'][0:titleLimit] + "...", "uri": song['uri']})
        elif itemCharLimitExceeded(song, "artist", "track") == 3:
            dictionary.append({"type": song["type"], "isDownloaded": False, "id": song['id'],
                               "artist": song['artist'][0:titleLimit] + "...",
                               "track": song['track'], "uri": song['uri']})
        else:
            dictionary.append(
                {"type": song["type"], "isDownloaded": False, "id": song['id'], "artist": song['artist'],
                 "track": song['track'], "uri": song['uri']})

    return dictionary


# endpoint to toggle the state of the current song
@app.put("/use/toggleplay")
async def toggle_music():
    if songPlayer.is_playing():
        songPlayer.pause()
        return
    else:
        songPlayer.play()


# endpoint for getting all songs
@app.get("use/searchall/{key}")
async def search_all(key: str):
    # sets up a connection to the database
    try:
        db = MySQLdb.connect("127.0.0.1", "newboxsql", "newbox", "songsdatabase")
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


# endpoint to debug and test functions
@app.get("/use/debug")
async def debug():
    return player.queue


# SPOTIFY FUNCTIONS
@app.get("/use/userDetails")
async def getUserDetails():
    return functions.getUserDetails()


@app.get("/use/getPlaybackInfo")
async def getPlaybackInfo():
    return functions.getPlaybackInfo()


# endpoint for pausing and playing music.
@app.put("/use/toggle")
async def toggle():
    player.toggle()


@app.put("/use/play")
async def play():
    player.play()


# endpoint for getting the current device that is playing spotify
@app.get("/use/getDevice")
async def getDevice():
    return functions.getDevice()


# endpoint for skipping tracks.
@app.put("/use/skip")
async def skip():
    return player.skip()


# endpoint for starting playback
@app.put("/use/playSong")
async def playSong():
    player.playSong()


# endpoint for
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
    return functions.searchFor(query, int(resultSize), returnType='artist')


@app.get("/use/getTopTracks")
async def getTopTracks():
    return functions.getTopTracks()


@app.get("/use/getTopArtists")
async def getTopArtists():
    return functions.getTopArtists()


@app.get("/use/getCategories")
async def getCategories():
    return functions.getCategories()


@app.get("/use/getArtistTopTracks/{artist}")
def getArtistTopTracks(artist):
    return functions.getTopSongsByArtist(artist)


@app.get("/use/getTrackCoverImage/{id}")
def getTrackCoverImage(id):
    return functions.getTrackCoverImage(id)


# LEDLIGHTS#

# https://stackoverflow.com/questions/57336022/make-an-addressable-led-strip-shift-from-one-pattern-to-the-next-after-a-set-amo

# endpoint for turning of the led lights
@app.put("/use/turnoff")
def turn_off():
    cmd = "{'status': 'off', 'music': 'off', 'color': '(0, 0, 0)'}" + '\n'
    arduinoData = serial.Serial('/dev/ttyUSB0', 1200)
    sleep(5)
    arduinoData.write(cmd.encode())
    return


@app.put("/use/nomusic")
async def no_music():
    cmd = "{'status': 'on', 'music': 'off', 'color': '(0, 0, 0)'}" + '\n'
    arduinoData = serial.Serial('/dev/ttyUSB0', 1200)
    sleep(5)
    arduinoData.write(cmd.encode())
    return


@app.get("/use/reboot")
async def reboot():
    os.system('sudo reboot')
    test = "Works"
    return test


@app.get("/use/shutdown")
async def shutdown():
    os.popen("sudo shutdown -h now").read()
    sleep(0.1)
    return


@app.put("/admin/remove/{uri}")
def removeFromQueue(uri):
    if uri in player.queue:
        if uri in player.queue[0]:
            player.skip()
        else:
            player.queue.remove(uri)


# To get the genre of a track and change LED colors based on what it is.
@app.put("/use/genre/{id}")
def get_track_color(id):
    url = functions.getTrackCoverImage(id)['img']
    tmp_file = 'tmp.jpg'

    """Downloads ths image file and analyzes the dominant color"""
    urlretrieve(url, tmp_file)
    color_thief = ColorThief(tmp_file)
    dominant_color = str(color_thief.get_color(quality=1))
    os.remove(tmp_file)
    cmd = "{'status': 'on', 'music': 'on', 'color': '" + (dominant_color) + "'}" + '\n'
    arduinoData = serial.Serial('/dev/ttyUSB0', 1200)
    sleep(5)
    arduinoData.write(cmd.encode())
    # returns rgb
    return


# endpoint for led light colors based on category
@app.put("/use/genre2/{name}")
async def change_genre(name: str):
    base16INT = int(name, 32)
    hexed = hex(base16INT)
    hexcode = '#' + hexed[2:][-6:].zfill(6)
    rgb = hex2rgb(hexcode)
    return json.dumps({"rgb": rgb})
