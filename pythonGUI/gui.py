import tkinter as tk
from tkinter import ttk
from tkinter import *

import requests


def btnClickFunction():
    url = "https://localhost:8000/use/playtest"
    response = requests.put(url)

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
    return

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


root = Tk()

root.geometry('1080x1920')
root.configure(background='#00ffff')
root.title('Newbox')

topBtnStyle = ttk.Style()
topBtnStyle.configure("custom.TButton", foreground="#42242C",
                      background="#42242C",
                       relief="none",
                      font= "Verdana 12",
                      radius= "10")

# searchbar

Entry(root, text='search').place(x=20, y=20)
#head buttons
Button(root, text='Playlist', font=('arial', 12, 'normal'), command=btnPlaylist()).place(x=20, y=130,width=500, height=100)
Button(root, text='Songs', font=('arial', 12, 'normal'), command=btnSongs()).place(x=560, y=130,width=500, height=100)
Button(root, text='Artists', font=('arial', 12, 'normal'), command=btnArtists()).place(x=20, y=240,width=500, height=100)
Button(root, text='Genres', font=('arial', 12, 'normal'), command=btnGenres()).place(x=560, y=240,width=500, height=100)
Button(root, text='Albums', font=('arial', 12, 'normal'), command=btnAlbums()).place(x=20, y=350,width=500, height=100)
Button(root, text='Downloads', command=btnDownloads()).place(x=560, y=350,width=500, height=100)

#style="topBtnStyle"

#footer buttons
Button(root, text='1', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn1()).place(x=10, y=1560,width=155, height=155)
Button(root, text='2', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn2()).place(x=190, y=1560,width=155, height=155)
Button(root, text='3', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn3()).place(x=370, y=1560,width=155, height=155)
Button(root, text='4', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn4()).place(x=550, y=1560,width=155, height=155)
Button(root, text='5', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn5()).place(x=730, y=1560,width=155, height=155)
Button(root, text='6', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btn6()).place(x=910, y=1560,width=155, height=155)
Button(root, text='reverse', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnPrevious()).place(x=10, y=1730,width=155, height=155)
Button(root, text='pause/play', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnPause()).place(x=190, y=1730,width=155, height=155)
Button(root, text='next', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnNext()).place(x=370, y=1730,width=155, height=155)
Button(root, text='mute', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnMute()).place(x=550, y=1730,width=155, height=155)
Button(root, text='volume down', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnSofter()).place(x=730, y=1730,width=155, height=155)
Button(root, text='volume up', bg='#FFFFFF', font=('arial', 12, 'normal'), command=btnHarder()).place(x=910, y=1730,width=155, height=155)

root.mainloop()