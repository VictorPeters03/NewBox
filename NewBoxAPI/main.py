import MySQLdb
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socket
import json
from spotifyAPI import functions

functions.getUserDetails()

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


# endpoint for setting the volume
@app.put("/adminpanel/volume/{amount}")
async def set_volume(amount: int):
    valid = False
    while not valid:
        try:
            volume = amount
            if (volume <= 100) and (volume >= 0):
                volume = json.dumps({"volume": amount})
                valid = True
            else:
                volume = json.dumps({"volume": "null"})
                valid = True
        except ValueError:
            valid = False
    return volume


# endpoint for setting the maximum volume
@app.put("/adminpanel/maxvolume/{amount}")
async def set_max_volume(amount: int):
    return


# endpoint for setting the minimum volume
@app.put("/adminpanel/minvolume/{amount}")
async def set_min_volume(amount: int):
    return


# endpoint for adding a song to the queue
@app.put("/use/queue/{id}")
async def add_to_queue(id: str):
    queue.append(id)


# endpoint for getting the queue
@app.get("/use/getqueue")
async def get_queue():
    return queue


@app.get("/use/play/{id}")
async def play_music(id: str):
    return


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
        dictionary.append({"id": song[0], "artist": song[1], "title": song[2], "uri": song[3]})

    return dictionary


# endpoint to toggle the state of the current song
@app.put("/use/toggleplay")
async def toggle_music():
    return


# endpoint for searching songs in the local database
@app.get("/use/search/{key}")
async def search_music(key: str):
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
        dictionary.append({"id": song[0], "artist": song[1], "title": song[2]})

    cursor.execute(sqlArtists, params)

    songs = cursor.fetchall()

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


@app.get("/play/userDetails")
async def getUserDetails():
    return functions.getUserDetails()


@app.get("/play/currentlyPlaying")
async def getCurrentlyPlaying():
    return functions.getPlaylistByName('test')