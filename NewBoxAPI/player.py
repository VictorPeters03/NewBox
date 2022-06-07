from time import sleep

import vlc
import threading

from spotifyAPI import functions

finish = 0

paused = False

queue = [
    r"spotify:track:4UDmDIqJIbrW0hMBQMFOsM",
    r"songs\Hello, how are you I am under the water.mp3",
    r"spotify:track:7GWU6dQFjYF5YpsAUwZfGq",
    r"songs\Pantera - Cowboys from Hell.mp3",
]

instance = vlc.Instance()
player = instance.media_player_new()


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
        queue.append(uri)
        newThread.start()
    else:
        queue.append(uri)


def SongFinished(event):
    global finish
    print("\nEvent reports - finished")
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
            duration = float(functions.getPlaybackInfo()['duration_seconds'])
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


newThread = threading.Thread(target=playSong)
newThread.start()
