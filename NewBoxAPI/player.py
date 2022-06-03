from time import sleep

import vlc
import threading

from NewBoxAPI.spotifyAPI import functions

finish = 0

paused = 0

queue = [
    r"songs\Hello, how are you I am under the water.mp3",
    r"spotify:track:5oD2Z1OOx1Tmcu2mc9sLY2",
    r"songs\Pantera - Cowboys from Hell.mp3",
]

instance = vlc.Instance()
player = instance.media_player_new()


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
            counter = 0
            while counter < duration:
                if not paused:
                    sleep(1)
                    counter += 1
                else:
                    sleep(1)
            queue.pop(0)


newThread = threading.Thread(target=playSong)
if len(queue) > 0:
    newThread.start()

x = input("pause ")
if x == "yes":
    player.pause()

y = input("play ")
if y == "yes":
    player.play()
