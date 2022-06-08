from time import sleep
import math
import vlc
import threading

from spotifyAPI import functions

finish = 0
counter = 1
paused = False

queue = []

instance = vlc.Instance()
player = instance.media_player_new()


def skip():
    global finish
    if len(queue) > 0:
        if "spotify" not in queue[0]:
            finish = 1
            queue.pop(0)
            player.stop()
        else:
            global counter
            functions.pause()
            counter = functions.getPlaybackInfo()['duration_seconds']

def pause():
    global paused
    if not paused:
        if "spotify" not in queue[0]:
            paused = True
            player.pause()
        else:
            paused = True
            functions.pause()


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
    if len(queue) == 0:
        newThread = threading.Thread(target=playSong)
        if "spotify" not in uri:
            newUri = "songs/" + uri
            queue.append(repr(newUri)[1:-1])
        else:
            queue.append(repr(uri)[1:-1])
        newThread.start()
    else:
        if "spotify" not in uri:
            newUri = "songs/" + uri
            queue.append(repr(newUri)[1:-1])
        else:
            queue.append(repr(uri)[1:-1])


def SongFinished(event):
    global finish
    print("\nEvent reports - finished")
    if queue:
        queue.pop(0)
    finish = 1


def playSong():
    while len(queue) > 0:
        if "spotify" not in queue[0]:
            media = instance.media_new_path(queue[0])
            player.set_media(media)
            events = player.event_manager()
            events.event_attach(vlc.EventType.MediaPlayerEndReached, SongFinished)
            global finish
            finish = 0
            player.play()
            while finish == 0:
                sleep(0.5)
        else:
            functions.play(queue[0])
            sleep(1)
            duration = math.floor(functions.getSongDuration(queue[0]))
            global counter
            counter = 1
            while counter < duration:
                if not paused:
                    sleep(1)
                    counter += 1
                    print(counter)
                else:
                    sleep(1)
                    print(counter)
            queue.pop(0)


