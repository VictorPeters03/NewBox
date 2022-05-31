import MySQLdb
from fastapi import FastAPI
import socket
import json
import alsaaudio
import spotipy
from authorization import spotifyHandler
from secrets import DEVICE_ID, USER

app = FastAPI()

max_volume = 100
min_volume = 0


# http://larsimmisch.github.io/pyalsaaudio/libalsaaudio.html#module-alsaaudio
# endpoint for setting the volume
@app.put("/adminpanel/volume/{amount}")
async def set_volume(amount: int):
    valid = False
    while not valid:
        try:
            if (amount <= max_volume) and (amount >= min_volume):
                mixer = alsaaudio.Mixer('PCM')
                mixer.setvolume(amount)
                volume = json.dumps({"volume": amount})
                valid = True
            elif amount > max_volume:
                volume = json.dumps({"volume": max_volume,
                                     "mess": "Input volume was higher than the maximum volume. Volume is set to the maximum volume."})
                valid = True
            elif amount < min_volume:
                volume = json.dumps({"volume": min_volume,
                                     "mess": "Input volume was lower than the minimum volume. Volume is set to the minimum volume."})
                valid = True
        except ValueError:
            valid = False
    return volume


# endpoint for setting the maximum volume
@app.put("/adminpanel/maxvolume/{amount}")
async def set_max_volume(amount: int):
    if (amount <= 100) and (amount >= 0) and (amount > min_volume):
        max_volume = amount
        mess = "Maximum volume is set to" + str(max_volume) + "."
    elif amount < min_volume:
        mess = "Maximum volume is lower than the minimum volume. That is not possible."
        max_volume = 100
    else:
        mess = "Maximum volume is not in the range of 0-100."
        max_volume = 100
    return json.dumps({"mess": mess, "max_volume": max_volume})


# endpoint for setting the minimum volume
@app.put("/adminpanel/minvolume/{amount}")
async def set_min_volume(amount: int):
    if (amount <= 100) and (amount >= 0) and (max_volume > amount):
        min_volume = amount
        mess = "Minimum volume is set to" + str(amount) + "."
    elif max_volume < amount:
        min_volume = 0
        mess = "Minimum volume is higher than the maximum volume. That is not possible."
    else:
        min_volume = 0
        mess = "Minimum volume is not in the range of 0-100."
    return json.dumps({"mess": mess, "min_volume": min_volume})


# endpoint for adding a song to the queue
@app.put("/use/queue/{id}")
async def add_to_queue(id: str):
    return


# endpoint for getting the queue
@app.get("/use/getqueue")
async def get_queue():
    return


# endpoint for playing songs
@app.get("/use/play/{id}")
async def play_music(id: str):
    return


# endpoint to toggle the state of the current song
@app.put("/use/toggleplay")
async def toggle_music():
    return


# endpoint to skip the current song
@app.put("/use/skip/{id}")
async def skip_song(id: str):
    return


# endpoint for searching individual songs in the local database
@app.get("/use/search/{key}")
async def search_music(id: str):
    # sets up a connection to the database
    try:
        db = MySQLdb.connect("127.0.0.1", "root", "", "djangosearchbartest")
    except:
        return "Can't connect to database"

    cursor = db.cursor()

    # the SQL statement
    sql = "SELECT * FROM `core_song` WHERE id = %s;"
    song_id = id

    # executes the statement
    cursor.execute(sql, song_id)

    # takes the data from the statement and places it in a variable
    songs = cursor.fetchall()

    db.close()

    dictionary = []

    for song in songs:
        dictionary.append({"id": song[0], "artist": song[1], "title": song[2]})

    return dictionary


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


# endpoint to debug and test functions
@app.get("/use/debug")
async def debug():
    return


# LEDLIGHTS#

# https://stackoverflow.com/questions/57336022/make-an-addressable-led-strip-shift-from-one-pattern-to-the-next-after-a-set-amo

# endpoint for turning of the led lights
@app.put("/use/turnoff")
async def turn_off():
    return


@app.put()
async def no_music():
    return


def getTrackGenre(name: str):
    def getTrackId(query):
        result = spotifyHandler.search(q=query, limit=1, type='track')
        return result['tracks']['items'][0]['id']

    def getTrackByID(trackName):
        track = getTrackId(trackName)
        return spotifyHandler.track(track)['uri']['artists']

    artist = getTrackByID.spotifyHandler.track(track["artists"][0]["external_urls"]["spotify"])
    genreString = print("artist genres:", artist["genres"])

    if genreString.find("pop"):
        # change Led color here
        return
    return


# endpoint for led light colors based on category
@app.put("/use/genre/{name}")
async def change_genre(name: str):
    # Add more elif statments for other main genres
    if name.find("pop"):
        # light color/pattern that the leds should display when playing this genre
        return
    elif name.find("classic"):
        return
    else:
        # When none of the substrings that are searched for in the genre name are found

        return
    return
