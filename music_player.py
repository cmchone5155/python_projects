import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicPlayer = tkr.Tk()
musicPlayer.title("My Music Player")
musicPlayer.geometry("450x350")
directory = askdirectory()
os.chdir(directory)
songList = os.listdir()

playList = tkr.Listbox(musicPlayer, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
for item in songList:
    pos = 0
    playList.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playList.get(tkr.ACTIVE))
    var.set(playList.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play,
bg="blue", fg="white")

Button2 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop,
bg="red", fg="white")

Button3 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause,
bg="purple", fg="white")

Button4 = tkr.Button(musicPlayer, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause,
bg="orange", fg="white")

var = tkr.StringVar()
songTitle = tkr.Label(musicPlayer, font="Helvetica 12 bold", textvariable=var)

songTitle.pack()

Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playList.pack(fill="both", expand="yes")
musicPlayer.mainloop()