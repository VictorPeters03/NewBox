import tkinter as tk
from tkinter import ttk
from tkinter import *
from background import GradientFrame
import requests
from functools import partial
import VerticalScrolledFrame

import random

transBackground = '#ABCABC'


def randomNumber():
    random_number = random.randint(1118481, 16777215)
    hex_number = str(hex(random_number))
    return '#' + hex_number[2:]


root = Tk()
# gf = GradientFrame(root, colors=("#4C0113", "black"), height=1920, width=1080)
gf = GradientFrame(root, colors=(randomNumber(), randomNumber()), height=1930, width=1090)
gf.config(direction=gf.top2bottom)
gf.pack()
root.geometry('1080x1920')

# root.attributes('-fullscreen',True)
# root.configure(background=hex_number)
root.title('Newbox')
# root.overrideredirect(True)
root.wm_attributes('-transparentcolor', transBackground)
root.wait_visibility(root)

URL_BASE = "https://localhost:8000/"


def btnClickFunction():
    endpoint = "use/playtest"
    response = requests.put(URL_BASE + endpoint)

    print(response.text)


def btnPlaylist():
    url = "https://localhost:8000/"
    return


def btnSongs():
    songs = requests.get("http://127.0.0.1:8000/use/getPlaylistItems/37i9dQZEVXbKCF6dqVpDkS")
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    for song in songs.json():
        songEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE, bg='#4A272E')
        songInfo = Frame(songEntry, height=2, bg="#4A272E")
        songQueue = Frame(songEntry, height=2)
        songArtist = Label(songInfo, text=song['artist'], relief='flat', borderwidth=4, font=('arial', 20),
                           bg="#4A272E", fg="#C7C7C7")
        margin = Label(songInfo, borderwidth=0, highlightthickness=0, height=2, bg='#4A272E')
        songTitle = Label(songInfo, text=song['track'], font=('arial', 30), bg="#4A272E", fg="#FFFFFF")

        songEntry.pack(fill=X)
        songInfo.pack(side=LEFT)
        songQueue.pack(side=RIGHT)
        songTitle.pack(anchor="w")
        margin.pack(anchor='w')
        songArtist.pack(anchor="w")
        Button(songQueue, text="add to queue", justify="right", command=partial(addToQueue, song["uri"])).pack(
            anchor='e')


def btnArtists():
    return


def btnGenres():
    return


def btnAlbums():
    return


def btnDownloads():
    songs = requests.get("http://127.0.0.1:8000/use/getsongs")
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    for song in songs.json():
        songEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE, bg='#4A272E')
        songInfo = Frame(songEntry, height=2, bg="#4A272E")
        songQueue = Frame(songEntry, height=2)
        songArtist = Label(songInfo, text=song['artist'], relief='flat', borderwidth=4, font=('arial', 20),
                           bg="#4A272E", fg="#C7C7C7")
        margin = Label(songInfo, borderwidth=0, highlightthickness=0, height=2, bg='#4A272E')
        songTitle = Label(songInfo, text=song['track'], font=('arial', 30), bg="#4A272E", fg="#FFFFFF")

        songEntry.pack(fill=X)
        songInfo.pack(side=LEFT)
        songQueue.pack(side=RIGHT)
        songTitle.pack(anchor="w")
        margin.pack(anchor='w')
        songArtist.pack(anchor="w")
        Button(songQueue, text="add to queue", justify="right", command=partial(addToQueue, song["uri"])).pack(
            anchor='e')


def btn1():
    return


def btn2():
    return


def btn3():
    return


def btn4():
    return


def btn5():
    return


def btn6():
    return


def btnPrevious():
    return


def btnPause():
    requests.put("http://127.0.0.1:8000/use/toggle")


def btnNext():
    # for widget in songList.winfo_children():
    #     widget.destroy()
    return


def btnMute():
    return


def btnSofter():
    return


def btnHarder():
    return


def searchSongs():
    songs = requests.get("http://127.0.0.1:8000/use/search/" + e.get())
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    for song in songs.json():
        if song['type'] == 'track':
            songEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE, bg='#4A272E')
            songInfo = Frame(songEntry, height=2, bg="#4A272E")
            songQueue = Frame(songEntry, height=2)
            songArtist = Label(songInfo, text=song['artist'], relief='flat', borderwidth=4, font=('arial', 20),
                               bg="#4A272E", fg="#C7C7C7")
            margin = Label(songInfo, borderwidth=0, highlightthickness=0, height=2, bg='#4A272E')
            songTitle = Label(songInfo, text=song['track'], font=('arial', 30), bg="#4A272E", fg="#FFFFFF")

            songEntry.pack(fill=X)
            songInfo.pack(side=LEFT)
            songQueue.pack(side=RIGHT)
            songTitle.pack(anchor="w")
            margin.pack(anchor='w')
            songArtist.pack(anchor="w")
            Button(songQueue, text="add to queue", justify="right", command=partial(addToQueue, song["uri"])).pack(
                anchor='e')


def addToQueue(uri):
    requests.put("http://127.0.0.1:8000/use/queue/" + uri)


topBtnStyle = ttk.Style()
topBtnStyle.configure("custom.TButton", foreground="#42242C",
                      background="#42242C",
                      relief="none",
                      font="Verdana 12",
                      radius="10")

# searchbar

# searchbar
btnCloseSearchBar = tk.PhotoImage(file='images/icons/Cross-small.png')
btnSearchSearchBar = tk.PhotoImage(file='images/icons/Search-small.png')

e = Entry(root, borderwidth=0, highlightthickness=0, background="#783FE3", foreground="white",
          font=('arial', 30, 'bold'), justify='center')
cross = Button(root, text="close", image=btnCloseSearchBar, background="#783FE3", borderwidth=0)
search = Button(root, text="search", image=btnSearchSearchBar, background="#783FE3", borderwidth=0, command=searchSongs)
e.place(width=911, x=84, y=40, height=80)
cross.place(width=70, height=80, x=930, y=40)
search.place(width=70, height=80, x=82, y=40)

# button images
btnImgPlaylist = tk.PhotoImage(file='images/btnPlaylist.png', height=100, width=500)
btnImgSongs = tk.PhotoImage(file='images/btnSongs.png', height=100, width=500)
btnImgArtist = tk.PhotoImage(file='images/btnArtist.png', height=100, width=500)
btnImgGenres = tk.PhotoImage(file='images/btnGenres.png', height=100, width=500)
btnImgAlbums = tk.PhotoImage(file='images/btnAlbums.png', height=100, width=500)
btnImgDownloaded = tk.PhotoImage(file='images/btnDownloaded.png', height=100, width=500)

# icons

iconImgPlaylist = tk.PhotoImage(file='images/icons/Playlist.png')
iconImgSongs = tk.PhotoImage(file='images/icons/Songs.png')
iconImgArtist = tk.PhotoImage(file='images/icons/Artist.png')
iconImgGenres = tk.PhotoImage(file='images/icons/Genre.png')
iconImgAlbums = tk.PhotoImage(file='images/icons/Albums.png')
iconImgDownloaded = tk.PhotoImage(file='images/icons/Download.png')

# text: arial, 30 bold white

# head buttons
Button(root, image=iconImgPlaylist, text="Playlist", anchor="w", padx=30, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnPlaylist, border=0, bg='#4A272E').place(x=84, y=130, width=436, height=100)
Button(root, image=iconImgSongs, text="Songs", anchor="w", padx=45, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnSongs, border=0, bg='#4A272E').place(x=560, y=130, width=436, height=100)
Button(root, image=iconImgArtist, text="Artist", anchor="w", padx=30, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnArtists, border=0, bg='#4A272E').place(x=84, y=240, width=436, height=100)
Button(root, image=iconImgGenres, text="Genres", anchor="w", padx=30, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnGenres, border=0, bg='#4A272E').place(x=560, y=240, width=436, height=100)
Button(root, image=iconImgAlbums, text="Albums", anchor="w", padx=30, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnAlbums, border=0, bg='#4A272E').place(x=84, y=350, width=436, height=100)
Button(root, image=iconImgDownloaded, text="Downloaded", anchor="w", padx=30, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnDownloads, border=0, bg='#4A272E').place(x=560, y=350, width=436, height=100)

# style="topBtnStyle"

# Downloaded songs
songs = requests.get("http://127.0.0.1:8000/use/getsongs")
# songList = Frame(root, height=1000, borderwidth=0, highlightthickness=0)
songList = VerticalScrolledFrame.VerticalScrolledFrame(root, bg='#4A272E')
songList.place(y=500, width=911, height=1000, x=84)
btnDownloads()

# footer buttons
Button(root, text='1', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btn1).place(x=10, y=1560,
                                                                                                           width=155,
                                                                                                           height=155)
Button(root, text='2', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btn2).place(x=190,
                                                                                                           y=1560,
                                                                                                           width=155,
                                                                                                           height=155)
Button(root, text='3', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btn3).place(x=370,
                                                                                                           y=1560,
                                                                                                           width=155,
                                                                                                           height=155)
Button(root, text='4', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btn4).place(x=550,
                                                                                                           y=1560,
                                                                                                           width=155,
                                                                                                           height=155)
Button(root, text='5', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btn5).place(x=730,
                                                                                                           y=1560,
                                                                                                           width=155,
                                                                                                           height=155)
Button(root, text='6', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btn6).place(x=910,
                                                                                                           y=1560,
                                                                                                           width=155,
                                                                                                           height=155)
Button(root, text='reverse', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btnPrevious).place(
    x=10, y=1730,
    width=155,
    height=155)
Button(root, text='pause/\nplay', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0,
       command=btnPause).place(x=190, y=1730,
                               width=155,
                               height=155)
Button(root, text='next', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btnNext).place(x=370,
                                                                                                                 y=1730,
                                                                                                                 width=155,
                                                                                                                 height=155)
Button(root, text='mute', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btnMute).place(x=550,
                                                                                                                 y=1730,
                                                                                                                 width=155,
                                                                                                                 height=155)
Button(root, text='volume\ndown', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0,
       command=btnSofter).place(x=730, y=1730,
                                width=155,
                                height=155)
Button(root, text='volume\nup', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0,
       command=btnHarder).place(x=910, y=1730,
                                width=155,
                                height=155)

root.mainloop()
