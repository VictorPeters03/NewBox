import os
import random
import tkinter as tk
from functools import partial
from tkinter import *
from tkinter import ttk

import requests
from PIL import ImageTk, Image

import VerticalScrolledFrame
from background import GradientFrame

xPadding = 20


def randomNumber():
    random_number = random.randint(1118481, 16777215)
    hex_number = str(hex(random_number))
    return '#' + hex_number[2:]


root = Tk()

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

gf = GradientFrame(root, colors=("#79090F", "#0c0146"), height=screenHeight, width=screenWidth,
                   highlightthickness=0)
gf.config(direction=gf.top2bottom)
gf.pack()

resolutionString = "%dx%d" % (screenWidth, screenHeight)
root.geometry(resolutionString)
root.attributes('-fullscreen', True)
root.title('Newbox')
root.wait_visibility(root)

URL_BASE = "https://localhost:8000/"


# Displays songs or artists in the list
def displayItems(items, type):
    if type == 'track':
        for item in items.json():
            songEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE,
                              bg='#4A272E', padx=xPadding)
            songInfo = Frame(songEntry, height=2, bg="#4A272E")
            songQueue = Frame(songEntry, height=2)
            songArtist = Label(songInfo, text=item['artist'], relief='flat', borderwidth=4, font=('arial', 20),
                               bg="#4A272E", fg="#C7C7C7")
            margin = Label(songInfo, borderwidth=0, highlightthickness=0, height=2, bg='#4A272E')
            songTitle = Label(songInfo, text=item['track'], font=('arial', 30), bg="#4A272E", fg="#FFFFFF")

            songEntry.pack(fill=X)
            songInfo.pack(side=LEFT)
            songQueue.pack(side=RIGHT)
            songTitle.pack(anchor="w")
            margin.pack(anchor='w')
            songArtist.pack(anchor="w")
            Button(songQueue, text="add to queue", image=iconImgPlaylist, border=0, highlightthickness=0,
                   background='#4A272E', justify="right", command=partial(addToQueue, item["uri"])).pack(
                anchor='e')
    else:
        for item in items.json():
            artistEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE,
                                bg='#4A272E', padx=xPadding)
            artistInfo = Frame(artistEntry, height=2, bg="#4A272E")
            artistLink = Frame(artistEntry, height=2)
            artistName = Label(artistInfo, text=item['name'], relief='flat', borderwidth=4, font=('arial', 30),
                               bg="#4A272E", fg="#FFFFFF")
            artistEntry.pack(fill=X)
            artistInfo.pack(side=LEFT)
            artistLink.pack(side=RIGHT)
            artistName.pack(anchor="w")
            Button(artistLink, text="get top songs", justify="right", border=0, highlightthickness=0,
                   image=artistGetTopSongsIcon, background='#4A272E', command=partial(getTopSongs, item["uri"])).pack(
                anchor='e')


# Is called when the songs button is pressed. Gets songs from the top 50.
def btnSongs():
    songs = requests.get("http://127.0.0.1:8000/use/getPlaylistItems/37i9dQZEVXbKCF6dqVpDkS")
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    displayItems(songs, 'track')


# Is called when the artists button is pressed. Gets top artist from the spotify account.
def btnArtists():
    artists = requests.get("http://127.0.0.1:8000/use/getTopArtists")
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    displayItems(artists, 'artist')


# Is called when the downloaded songs button is pressed. Gets the downloaded songs.
def btnDownloads():
    songs = requests.get("http://127.0.0.1:8000/use/getsongs")
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    displayItems(songs, 'track')


# Is called when the queue button is pressed. Gets the songs in the queue.
def btnGetQueue():
    queuedSongs = requests.get("http://127.0.0.1:8000/use/getQueue")
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    if len(queuedSongs.json()) != 0:
        for song in queuedSongs.json():
            songEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE,
                              bg='#4A272E', padx=xPadding)
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


# Is called when the pause button is pressed.
def btnPause():
    requests.put("http://127.0.0.1:8000/use/toggle")


# Is called when the mute button is pressed.
def btnMute():
    requests.get("http://127.0.0.1:8000/adminpanel/togglemute")
    return


# Is called when the volume down button is pressed.
def btnSofter():
    requests.put("http://127.0.0.1:8000/adminpanel/volume/softer")
    return


# Is called when the volume up button is pressed.
def btnHarder():
    requests.put("http://127.0.0.1:8000/adminpanel/volume/harder")
    return


# Is called when a song is searched.
def searchSongs():
    songs = requests.get("http://127.0.0.1:8000/use/search/" + e.get())
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    for song in songs.json():
        if song['type'] == 'track':
            songEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE,
                              bg='#4A272E', padx=xPadding)
            songInfo = Frame(songEntry, height=2, bg="#4A272E")
            songQueue = Frame(songEntry, height=2)

            songArtist = Label(songInfo, text=song['artist'], relief='flat', borderwidth=4, font=('arial', 20),
                               bg="#4A272E", fg="#C7C7C7")
            margin = Label(songInfo, borderwidth=0, highlightthickness=0, height=2, bg='#4A272E')
            songTitleImage = Frame(songInfo, borderwidth=0, highlightthickness=0, bg="#4A272E")
            downloadedLabel = Label(songTitleImage, image=songIcon, bg="#4A272E")
            spotifyLabel = Label(songTitleImage, image=spotifyIcon, bg="#4A272E")
            songTitle = Label(songTitleImage, text=song['track'], font=('arial', 30), bg="#4A272E", fg="#FFFFFF")

            songEntry.pack(fill=X)
            songInfo.pack(side=LEFT)
            songQueue.pack(side=RIGHT)
            songTitleImage.pack(anchor=W)
            if song['isDownloaded']:
                downloadedLabel.pack(side=LEFT)
            else:
                spotifyLabel.pack(side=LEFT)
            margin.pack(anchor='w')
            songTitle.pack(anchor="w")
            songArtist.pack(anchor="w")
            Button(songQueue, image=iconImgPlaylist, border=0, highlightthickness=0, text="add to queue",
                   background='#4A272E',
                   justify="right", command=partial(addToQueue, song["uri"])).pack(
                anchor='e')
        elif song['type'] == 'artist':
            artistEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE,
                                bg='#4A272E', padx=xPadding)
            artistInfo = Frame(artistEntry, height=2, bg="#4A272E")
            artistLink = Frame(artistEntry, height=2)
            artistName = Label(artistInfo, text=song['artist'], relief='flat', borderwidth=4, font=('arial', 30),
                               bg="#4A272E", fg="#FFFFFF")
            artistEntry.pack(fill=X)
            artistInfo.pack(side=LEFT)
            artistLink.pack(side=RIGHT)
            artistName.pack(anchor="w")
            Button(artistLink, text="get top songs", image=artistGetTopSongsIcon, border=0, highlightthickness=0,
                   justify="right", background='#4A272E',
                   command=partial(getTopSongs, song["uri"])).pack(anchor='e')


def addToQueue(uri):
    requests.put("http://127.0.0.1:8000/use/queue/" + uri)


# Gets an artist's top songs.
def getTopSongs(uri):
    artistSongs = requests.get("http://127.0.0.1:8000/use/getArtistTopTracks/" + uri)
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    for song in artistSongs.json():
        songEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE,
                          bg='#4A272E', padx=xPadding)
        songInfo = Frame(songEntry, height=2, bg="#4A272E")
        songQueue = Frame(songEntry, height=2)
        margin = Label(songInfo, borderwidth=0, highlightthickness=0, height=2, bg='#4A272E')
        songTitle = Label(songInfo, text=song['track'], font=('arial', 30), bg="#4A272E", fg="#FFFFFF")

        songEntry.pack(fill=X)
        songInfo.pack(side=LEFT)
        songQueue.pack(side=RIGHT)
        songTitle.pack(anchor="w")
        margin.pack(anchor='w')
        Button(songQueue, image=iconImgPlaylist, text="add to queue", border=0, highlightthickness=0, justify="right",
               background='#4A272E',
               command=partial(addToQueue, song["uri"])).pack(anchor='e')


def convertToRGBA(path):
    return Image.open(path).convert("RGBA")


topBtnStyle = ttk.Style()
topBtnStyle.configure("custom.TButton", foreground="#42242C",
                      background="#42242C",
                      relief="none",
                      font="Verdana 12",
                      radius="10")


def closeSearchBar():
    os.system('bash ./toggle-matchbox.sh')
    e.place_forget()
    cross.place_forget()
    search.place_forget()
    logo.place(width=436, height=100, x=82, y=40)
    btnSearch.place(width=70, height=100, x=930, y=40)


def openSearchBar():
    os.system('bash ./toggle-matchbox.sh')
    logo.place_forget()
    btnSearch.place_forget()
    e.place(width=911, height=80, x=84, y=40)
    e.focus()
    cross.place(width=70, height=80, x=930, y=40)
    search.place(width=70, height=80, x=82, y=40)


root.bind("<Return>", lambda event: searchSongs())

# searchbar images
btnCloseSearchBar = tk.PhotoImage(file='images/icons/Cross-small.png')
btnSearchSearchBar = tk.PhotoImage(file='images/icons/Search-small.png')
iconBtnSearch = tk.PhotoImage(file='images/icons/Search.png')
logoImage = Image.open("images/Logo.png").resize((436, 100), Image.ANTIALIAS)
logoImageLabel = ImageTk.PhotoImage(logoImage)

e = Entry(root, borderwidth=0, highlightthickness=0, background="#783FE3", foreground="white",
          font=('arial', 30, 'bold'), justify='center')
cross = Button(root, text="close", image=btnCloseSearchBar, background="#783FE3", borderwidth=0, command=closeSearchBar,
               height=80, width=70)
search = Button(root, text="search", image=btnSearchSearchBar, background="#783FE3", borderwidth=0, command=searchSongs,
                height=80, width=70)
logo = Label(root, image=logoImageLabel, borderwidth=0, width=436, height=100, bg='#700813')
btnSearch = Button(root, image=iconBtnSearch, borderwidth=0, command=openSearchBar, height=80, width=70, bg='#700813')
logo.place(width=436, height=100, x=82, y=40)
btnSearch.place(width=70, height=100, x=930, y=40)

songIcon = ImageTk.PhotoImage(Image.open("images/icons/DownloadedSong.png"))
spotifyIcon = ImageTk.PhotoImage(Image.open("images/icons/SpotifySong.png"))
artistGetTopSongsIcon = ImageTk.PhotoImage(Image.open("images/icons/Arrow.png"))
# header icons

iconImgPlaylist = tk.PhotoImage(file='images/icons/Playlist.png')
iconImgSongs = tk.PhotoImage(file='images/icons/Songs.png')
iconImgArtist = tk.PhotoImage(file='images/icons/Artist.png')
iconImgDownloaded = tk.PhotoImage(file='images/icons/Download.png')

# footer icons
iconImgPlayPause = tk.PhotoImage(file='images/Play-Pause.png')
iconImgVolumeUp = tk.PhotoImage(file='images/Volume Up.png')
iconImgVolumeDown = tk.PhotoImage(file='images/Volume Down.png')
iconImgVolumeMute = tk.PhotoImage(file='images/Volume Mute.png')

# head buttons
Button(root, image=iconImgSongs, text="Songs", anchor="w", padx=45, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnSongs, border=0, bg='#4A272E').place(x=560, y=220, width=436, height=100)
Button(root, image=iconImgArtist, text="Artist", anchor="w", padx=30, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnArtists, border=0, bg='#4A272E').place(x=84, y=220, width=436, height=100)
Button(root, image=iconImgDownloaded, text="Downloaded", anchor="w", padx=30, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnDownloads, border=0, bg='#4A272E').place(x=84, y=330, width=436, height=100)
Button(root, image=iconImgPlaylist, text="Queue", anchor="w", padx=45, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnGetQueue, border=0, bg='#4A272E').place(x=560, y=330, width=436, height=100)

# style="topBtnStyle"

# Downloaded songs
songs = requests.get("http://127.0.0.1:8000/use/getsongs")
songList = VerticalScrolledFrame.VerticalScrolledFrame(root, bg='#4A272E', border=0, highlightthickness=0)
songList.place(y=500, width=911, height=1000, x=84)
btnDownloads()

# footer buttons

Button(root,
       text='pause/\nplay',
       bg='#4A272E',
       fg='white',
       font=('arial', 30, 'bold'),
       image=iconImgPlayPause,
       border=0,
       command=btnPause).place(x=84, y=1530, width=436, height=155)

Button(root,
       text='mute',
       bg='#4A272E',
       fg='white',
       font=('arial', 30, 'bold'),
       image=iconImgVolumeMute,
       border=0,
       command=btnMute).place(x=560, y=1530, width=436, height=155)

Button(root,
       text='volume\ndown',
       bg='#4A272E',
       fg='white',
       font=('arial', 30, 'bold'),
       image=iconImgVolumeDown,
       border=0,
       command=btnSofter).place(x=84, y=1730, width=436, height=155)

Button(root,
       text='volume\nup',
       bg='#4A272E',
       fg='white',
       font=('arial', 30, 'bold'),
       image=iconImgVolumeUp,
       border=0,
       command=btnHarder).place(x=560, y=1730, width=436, height=155)

root.mainloop()
