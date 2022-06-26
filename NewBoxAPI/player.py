from time import sleep
import math
import MySQLdb
import requests.exceptions
import vlc
import threading
import main

from spotifyAPI import functions

finish = 0
counter = 1
paused = False

queue = []

instance = vlc.Instance()
player = instance.media_player_new()


def filterQueue():
    global queue
    if functions.getDevice() is None:
        queue[:] = (uri for uri in queue if 'spotify' not in uri)
        # for count, uri in enumerate(queue):
        #     if 'spotify' in uri:
        #         queue.pop(count)
    return queue


def getQueue():
    info = []
    if not queue:
        return "Queue is empty"
    for uri in queue:
        songInfo = {}
        if 'spotify' in uri:
            try:
                song = functions.getSongByUri(uri)['name'] if len(functions.getSongByUri(uri)['name']) <= 40 else functions.getSongByUri(uri)['name'][0:40] + "..."
                artist = functions.getSongByUri(uri)['artist']
                songInfo.update({'uri': uri,
                                 'track': song,
                                 'artist': artist})
                info.append(songInfo)
            except KeyError:
                songInfo.update({'uri': uri,
                                 'message': 'Failed to get info from from spotify, check internet connection'})
                info.append(songInfo)
        else:
            result = getInfoFromDb(uri)
            song = result[1]
            artist = result[0]
            songInfo.update({'uri': uri,
                             'track': song,
                             'artist': artist})
            info.append(songInfo)
    return info


def getInfoFromDb(uri):
    try:
        db = MySQLdb.connect("127.0.0.1", "newboxsql", "newbox", "songsdatabase")
    except:
        return "Can't connect to database"

    cursor = db.cursor()

    # the SQL statement
    sql = "SELECT artist, song FROM `core_song` WHERE uri = %s;"
    params = [uri]
    cursor.execute(sql, params)
    songs = cursor.fetchall()
    db.close()
    songList = []
    for song in songs:
        songList.append(song[0])
        songList.append(song[1])
    return songList


# If there is no connection, skip button must be disabled
def skip():
    global finish
    if len(queue) > 0:
        if "spotify" in queue[0] and functions.getDevice() is not None:
            global counter
            functions.pause()
            counter = functions.getSongByUri(queue[0])['duration']
        elif "spotify" not in queue[0]:
            finish = 1
            queue.pop(0)
            player.stop()
        else:
            for i in range(len(getQueue())):
                if 'message' in getQueue()[0].keys():
                    queue.pop(0)


def toggle():
    global paused
    global counter
    if not queue:
        return
    if not paused:
        if "spotify" not in queue[0]:
            paused = True
            player.pause()
        else:
            paused = True
            functions.pause()
            counter = functions.getPlaybackInfo()['progress_seconds']
        return "Paused"
    else:
        if "spotify" not in queue[0]:
            paused = False
            player.pause()
        else:
            paused = False
            functions.pause()
        return "Resumed"


def play():
    global paused
    if paused:
        if "spotify" not in queue[0]:
            paused = False
            player.pause()
        else:
            paused = False
            functions.pause()


def addToQueue(uri):
    if len(queue) == 5 or uri in queue:
        return "Queue limit reached or song is already in queue"

    if len(queue) == 0:
        newThread = threading.Thread(target=playSong)
        if "spotify" not in uri:
            newUri = uri
            queue.append(repr(newUri)[1:-1])
        else:
            if functions.getDevice() is None or isinstance(functions.getDevice(), dict):
                return "Could not add spotify song, check internet connection"
            queue.append(repr(uri)[1:-1])
        newThread.start()
    else:
        if "spotify" not in uri:
            newUri = uri
            queue.append(repr(newUri)[1:-1])
        else:
            if functions.getDevice() is None or isinstance(functions.getDevice(), dict):
                return "Could not add spotify song, check internet connection"
            queue.append(repr(uri)[1:-1])


def SongFinished(event):
    global finish
    print("\nEvent reports - finished")
    if queue:
        queue.pop(0)
    isQueueEmpty()
    finish = 1


def isQueueEmpty():
    if not queue:
        requests.put(f"http://127.0.0.1:8000/use/nomusic")


def playSong():
    while len(queue) > 0:
        if "spotify" not in queue[0]:
            media = instance.media_new_path("songs/" + queue[0])
            player.set_media(media)
            events = player.event_manager()
            events.event_attach(vlc.EventType.MediaPlayerEndReached, SongFinished)
            global finish
            finish = 0
            player.play()
            requests.put(f"http://127.0.0.1:8000/use/nomusic")
            while finish == 0:
                sleep(0.5)
        else:
            if functions.getDevice() is None:
                skip()
                continue
            functions.play(queue[0])
            info = functions.getPlaybackInfo()['id']
            main.get_track_color(info)
            sleep(1)
            duration = functions.getSongDuration(queue[0])
            if isinstance(duration, dict):
                return
            duration = math.floor(duration)
            global counter
            counter = 1
            while counter < duration:
                if not paused:
                    if counter % 10 == 0 and functions.getDevice() is None:
                        skip()
                        counter = duration
                    sleep(1)
                    counter += 1
                    print(counter)
                else:
                    sleep(1)
                    print(counter)
            if functions.getDevice() is not None:
                queue.pop(0)
                isQueueEmpty()
