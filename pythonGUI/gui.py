import tkinter as tk
from tkinter import ttk
from tkinter import *
from background import GradientFrame
import requests

import random

random_number = random.randint(1118481, 16777215)
hex_number = str(hex(random_number))
hex_number = '#' + hex_number[2:]

URL_BASE = "http://127.0.0.1:8000/"


def btnClickFunction():
    endpoint = "use/playtest"
    response = requests.put(URL_BASE + endpoint)

    print(response.text)


def btnPlaylist():
    url = "https://localhost:8000/"
    return


def btnSongs():
    return


def btnArtists():
    return


def btnGenres():
    return


def btnAlbums():
    return


def btnDownloads():
    songs = requests.get("http://127.0.0.1:8000/use/getsongs")
    songList = Frame(root)
    songList.place(y=500, width=911, x=84)
    canvas = Canvas(songList)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    vbar = Scrollbar(songList, orient=VERTICAL, command=canvas.yview)
    vbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=vbar.set)
    canvas.bind('<Configure>', lambda f: canvas.configure(scrollregion=canvas.bbox("all")))
    canvasFrame = Frame(canvas)
    canvas.create_window((0, 0), window=canvasFrame, anchor=NW)
    for index, song in enumerate(songs.json()):
        mainframe = Frame(canvasFrame, height=80, width=911, borderwidth=2, relief=GROOVE)
        mainframe.grid(row=index)
        frame = Frame(mainframe, height=800)
        frame.grid(row=0, column=0)
        artist = Label(frame, text=song["artist"], font=('arial', 20))
        artist.grid(row=0, column=0)
        title = Label(frame, text=song["title"], font=('arial', 15))
        title.grid(row=1, column=0)
        queue = Label(frame, text="add to queue")
        queue.grid(row=0, column=1)
        # Button(canvasFrame, text=index).grid(row=index)


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
    return


def btnNext():
    return


def btnMute():
    return


def btnSofter():
    return


def btnHarder():
    return


def searchSongs():
    print(requests.get("http://127.0.0.1:8000/use/search/" + e.get()))


root = Tk()
gf = GradientFrame(root, colors=("#4C0113", "black"), height=1920, width=1080)
gf.config(direction=gf.top2bottom)
gf.pack()
root.geometry('1080x1920')
# root.attributes('-fullscreen',True)
# root.configure(background=hex_number)
root.title('Newbox')
root.wm_attributes()

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
Button(root, image=iconImgPlaylist, text="hallo", font=('arial', 30, 'bold'), compound=tk.LEFT, command=btnPlaylist,
       border=0, bg='#4A272E').place(x=20, y=130, width=500, height=100)
Button(root, image=iconImgSongs, text="hallo", font=('arial', 30, 'bold'), compound=tk.LEFT, command=btnSongs, border=0,
       bg='#4A272E').place(x=560, y=130, width=500, height=100)
Button(root, image=iconImgArtist, text="hallo", font=('arial', 30, 'bold'), compound=tk.LEFT, command=btnArtists,
       border=0, bg='#4A272E').place(x=20, y=240, width=500, height=100)
Button(root, image=iconImgGenres, text="hallo", font=('arial', 30, 'bold'), compound=tk.LEFT, command=btnGenres,
       border=0, bg='#4A272E').place(x=560, y=240, width=500, height=100)
Button(root, image=iconImgAlbums, text="hallo", font=('arial', 30, 'bold'), compound=tk.LEFT, command=btnAlbums,
       border=0, bg='#4A272E').place(x=20, y=350, width=500, height=100)
Button(root, image=iconImgDownloaded, text="hallo", font=('arial', 30, 'bold'), compound=tk.LEFT, command=btnDownloads,
       border=0, bg='#4A272E').place(x=560, y=350, width=500, height=100)

# style="topBtnStyle"

#Downloaded songs

# footer buttons
Button(root, text='1', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn1).place(x=10, y=1560, width=155,
                                                                                       height=155)
Button(root, text='2', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn2).place(x=190, y=1560, width=155,
                                                                                       height=155)
Button(root, text='3', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn3).place(x=370, y=1560, width=155,
                                                                                       height=155)
Button(root, text='4', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn4).place(x=550, y=1560, width=155,
                                                                                       height=155)
Button(root, text='5', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn5).place(x=730, y=1560, width=155,
                                                                                       height=155)
Button(root, text='6', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn6).place(x=910, y=1560, width=155,
                                                                                       height=155)
Button(root, text='reverse', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnPrevious).place(x=10, y=1730,
                                                                                                    width=155,
                                                                                                    height=155)
Button(root, text='pause/play', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnPause).place(x=190, y=1730,
                                                                                                    width=155,
                                                                                                    height=155)
Button(root, text='next', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnNext).place(x=370, y=1730, width=155,
                                                                                             height=155)
Button(root, text='mute', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnMute).place(x=550, y=1730, width=155,
                                                                                             height=155)
Button(root, text='volume down', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnSofter).place(x=730, y=1730,
                                                                                                      width=155,
                                                                                                      height=155)
Button(root, text='volume up', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnHarder).place(x=910, y=1730,
                                                                                                    width=155,
                                                                                                    height=155)

root.mainloop()
