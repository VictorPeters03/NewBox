import MySQLdb
from fastapi import FastAPI
import socket
import json
import alsaaudio
import os

app = FastAPI()

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
                mixer = alsaaudio.Mixer('PCM')
                mixer.setvolume(amount)
                volume = json.dumps({"volume": amount})
                valid = True
            elif amount > limits[1]:
                 volume = json.dumps({"volume": limits[1], "mess": "Input volume was higher than the maximum volume. Volume is set to the maximum volume."})
                 valid = True
            elif amount < limits[0]:
                volume = json.dumps({"volume": limits[0], "mess": "Input volume was lower than the minimum volume. Volume is set to the minimum volume."})
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
@app.put("/use/queue/{id}")
async def add_to_queue(id: str):
    queue.append(id)
    return


# endpoint for getting the queue
@app.get("/use/getqueue")
async def get_queue():
    return queue


# endpoint for playing songs
@app.get("/use/play/{id}")
async def play_music(id: str):
    return


# endpoint to toggle the state of the current song
@app.put("/use/toggleplay")
async def toggle_music():
    return


#endpoint to skip the current song
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
