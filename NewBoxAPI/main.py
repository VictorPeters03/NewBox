import MySQLdb
from fastapi import FastAPI
import socket
import json

app = FastAPI()

# endpoint for setting the volume
@app.put("/adminpanel/volume/{amount}")
async def set_volume(amount: int):
    valid = False
    while not valid:
        try:
            volume = int(amount)            
            if (volume <= 100) and (volume >= 0):
                volume = json.dumps({"volume": amount})
                valid = True
            else: 
                 volume = json.dumps({"volume": "null"})
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

# endpoint for searching songs in the local database
@app.get("/use/search/{key}")
async def search_music(key: str):
    return


# endpoint for getting the ip off the rpi
@app.get("/adminpanel/ip")
async def get_ip():
    return json.dumps({"ip": socket.gethostbyname(socket.gethostname())})

# endpoint to toggle the state of the current song
@app.get("/use/debug")
async def debug():

    try:
        db = MySQLdb.connect("127.0.0.1", "root", "", "djangosearchbartest")
    except:
        return "Can't connect to database"
    print("Connection established")

    cursor = db.cursor()

    sql = "SELECT * FROM `core_song`;"

    cursor.execute(sql)

    songs = cursor.fetchall()

    db.close()

    jsonString = json.dumps(songs)

    return jsonString
