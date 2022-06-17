import tkinter as tk
from tkinter import ttk
from tkinter import *
from background import GradientFrame
import requests
from functools import partial
import VerticalScrolledFrame
from PIL import ImageTk, Image

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
# root.wm_attributes('-transparentcolor', transBackground)
root.wait_visibility(root)

URL_BASE = "https://localhost:8000/"


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
    artists = requests.get("http://127.0.0.1:8000/use/getTopArtists")
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    for artist in artists.json():
        artistEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE,
                            bg='#4A272E')
        artistInfo = Frame(artistEntry, height=2, bg="#4A272E")
        artistLink = Frame(artistEntry, height=2)
        artistName = Label(artistInfo, text=artist['name'], relief='flat', borderwidth=4, font=('arial', 30),
                           bg="#4A272E", fg="#FFFFFF")
        artistEntry.pack(fill=X)
        artistInfo.pack(side=LEFT)
        artistLink.pack(side=RIGHT)
        artistName.pack(anchor="w")
        Button(artistLink, text="get top songs", justify="right", command=partial(getTopSongs, artist["uri"])).pack(
            anchor='e')


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


def btnPause():
    requests.put("http://127.0.0.1:8000/use/toggle")


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
            songEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE,
                              bg='#4A272E')
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
            Button(songQueue, text="add to queue", justify="right", command=partial(addToQueue, song["uri"])).pack(
                anchor='e')
        elif song['type'] == 'artist':
            artistEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE,
                                bg='#4A272E')
            artistInfo = Frame(artistEntry, height=2, bg="#4A272E")
            artistLink = Frame(artistEntry, height=2)
            artistName = Label(artistInfo, text=song['artist'], relief='flat', borderwidth=4, font=('arial', 30),
                               bg="#4A272E", fg="#FFFFFF")
            artistEntry.pack(fill=X)
            artistInfo.pack(side=LEFT)
            artistLink.pack(side=RIGHT)
            artistName.pack(anchor="w")
            Button(artistLink, text="get top songs", justify="right", command=partial(getTopSongs, song["uri"])).pack(
                anchor='e')



def addToQueue(uri):
    requests.put("http://127.0.0.1:8000/use/queue/" + uri)


def getTopSongs(uri):
    artistSongs = requests.get("http://127.0.0.1:8000/use/getArtistTopTracks/" + uri)
    songList.resetY()
    for widget in songList.interior.winfo_children():
        widget.destroy()
    for song in artistSongs.json():
        songEntry = Frame(songList.interior, height=187, pady=30, borderwidth=1, width=911, relief=RIDGE, bg='#4A272E')
        songInfo = Frame(songEntry, height=2, bg="#4A272E")
        songQueue = Frame(songEntry, height=2)
        # songArtist = Label(songInfo, text=song['artist'], relief='flat', borderwidth=4, font=('arial', 20),
        #                    bg="#4A272E", fg="#C7C7C7")
        margin = Label(songInfo, borderwidth=0, highlightthickness=0, height=2, bg='#4A272E')
        songTitle = Label(songInfo, text=song['track'], font=('arial', 30), bg="#4A272E", fg="#FFFFFF")

        songEntry.pack(fill=X)
        songInfo.pack(side=LEFT)
        songQueue.pack(side=RIGHT)
        songTitle.pack(anchor="w")
        margin.pack(anchor='w')
        # songArtist.pack(anchor="w")
        Button(songQueue, text="add to queue", justify="right", command=partial(addToQueue, song["uri"])).pack(
            anchor='e')


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

searchBarBox = Frame(root, borderwidth=0, highlightthickness=0, height=80)
e = Entry(searchBarBox, borderwidth=0, highlightthickness=0, background="#783FE3", foreground="white",
          font=('arial', 30, 'bold'), justify='center')
cross = Button(root, text="close", image=btnCloseSearchBar, background="#783FE3", borderwidth=0)
search = Button(root, text="search", image=btnSearchSearchBar, background="#783FE3", borderwidth=0, command=searchSongs)
searchBarBox.place(width=911, x=84, y=40)
e.place(width=911, height=80)
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
songIcon = ImageTk.PhotoImage(Image.open("images/icons/DownloadedSong.png"))
spotifyIcon = ImageTk.PhotoImage(Image.open("images/icons/SpotifySong.png"))

# text: arial, 30 bold white

# head buttons
Button(root, image=iconImgSongs, text="Songs", anchor="w", padx=45, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnSongs, border=0, bg='#4A272E').place(x=560, y=130, width=436, height=100)
Button(root, image=iconImgArtist, text="Artist", anchor="w", padx=30, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnArtists, border=0, bg='#4A272E').place(x=84, y=130, width=436, height=100)
Button(root, image=iconImgDownloaded, text="Downloaded", anchor="w", padx=30, fg='white', font=('arial', 30, 'bold'),
       compound=tk.LEFT, command=btnDownloads, border=0, bg='#4A272E').place(x=84, y=240, width=912, height=100)

# style="topBtnStyle"

# Downloaded songs
songs = requests.get("http://127.0.0.1:8000/use/getsongs")
# songList = Frame(root, height=1000, borderwidth=0, highlightthickness=0)
songList = VerticalScrolledFrame.VerticalScrolledFrame(root, bg='#4A272E')
songList.place(y=500, width=911, height=1000, x=84)
btnDownloads()

# footer buttons

# Button(root, text='reverse', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btnPrevious).place(
#     x=10, y=1730,
#     width=155,
#     height=155)
Button(root, text='pause/\nplay', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0,
       command=btnPause).place(x=190, y=1730,
                               width=155,
                               height=155)
# Button(root, text='next', bg='#4A272E', fg='white', font=('arial', 30, 'bold'), border=0, command=btnNext).place(x=370,
#                                                                                                                  y=1730,
#                                                                                                                  width=155,
#                                                                                                                  height=155)
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
