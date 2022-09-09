import tkinter as tk
from tkinter import filedialog
from threading import *
from tkinter import ttk
from ctypes import windll
from pytube import YouTube
import shutil
import time
import os
def onclick(event):
    dir = filedialog.askdirectory()
    os.chdir(dir)
    dir_select.config(text = dir)

def delete_placeholer(event):
    link_receiver.delete(0, 'end')

#Close window
def close_window(event):
    main.title('Thanks for using my software UwU')
    time.sleep(.5)
    main.destroy()

#Download video files:
def Download_Vid(event):
    linkVid = link_receiver.get()
    mp4 = YouTube(linkVid)
    mp4.streams.filter(adaptive = True, file_extension = 'mp4')
    stream = mp4.streams.get_highest_resolution()
    stream.download()

#Download audio files:
def Download_Audio(event):
    link_audio = link_receiver.get()
    mp3 = YouTube(link_audio)
    stream = mp3.streams.filter(only_audio = True, file_extension ='webm').first()
    stream.download()

#Pin to top:
def Pin_win(event):
    main.attributes('-topmost',1)

#Unpin
def Unpin_win(event):
    main.attributes('-topmost',0)
#GUI control
try:
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    main = tk.Tk()
    main.title('Youtube Downloader')
    main.iconbitmap('youtube.ico')
    main.geometry('1280x720+300+150')
    main.resizable(False, False)
    welcome = ttk.Label(main,text = 'Welcome to the Youtube Downloader', font = ("Segoe UI", 20, 'bold'),foreground="red")
    note = ttk.Label(main,text = 'Note: You might experience lag while downloading, please be patient!', font = ("Segoe UI", 12, 'bold', 'italic'))
    disclaimer = ttk.Label(main,text = 'Disclaimer: I hold no responsibility whatsoever to those whose abuse this software for accessing license-protected videos/audio', font = ("Segoe UI", 12, 'bold','italic'))
    welcome.pack()
    note.pack()
    disclaimer.pack()
    link_receiver = ttk.Entry(main,width = 100)
    link_receiver.pack(ipady = 10,ipadx = 120, pady = 100)
    link_receiver.insert(0,'Paste Youtube link to clipboard')
    link_receiver.bind('<FocusIn>', delete_placeholer)
    dir_select = ttk.Button(main,text = "Select save directory")
    dir_select.bind('<Button>', onclick)
    dir_select.pack()
    Download_vid = ttk.Button(main,text = 'Download Video')
    Download_audio = ttk.Button(main,text = 'Download Audio')
    quit = ttk.Button(main,text = 'Quit')
    unpin = ttk.Button(main,text = 'Unpin me!')
    pin = ttk.Button(main,text = 'Pin me!')
    Download_vid.pack(ipadx = 10, ipady = 5)
    Download_audio.pack(ipadx = 10, ipady = 5)
    quit.pack(ipadx = 10, ipady = 5)
    pin.pack()
    unpin.pack()
    pin.place(x = 0, y = 0)
    unpin.place(x = 1210, y = 0)
    pin.bind('<Button>', Pin_win)
    unpin.bind('<Button>', Unpin_win)
    Download_vid.bind('<Button>',Download_Vid)
    Download_audio.bind('<Button>',Download_Audio)
    quit.bind('<Button>',close_window)
    main.mainloop()
    tk.mainloop()
