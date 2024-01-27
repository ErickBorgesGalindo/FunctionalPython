from pytube import YouTube
from pytube import *
import pytube
from tkinter import *
from tkinter import messagebox as Messagebox
from PIL import Image, ImageTk

#-------- Descargar videos -----------
def video():
    import os
    link = videos.get()
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    yt.download()
    print("Descarga con éxito")

def video_playlist():
    import os
    #Escribir playlist a descargar
    link = videos.get()
    playlist=Playlist(link)
    print(playlist)
    for video in playlist.videos:
        url=video.watch_url
        yt = pytube.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = stream.download()
        print("Video descargado como ", filename)
    print("Playlist descargada")

    
#----------- Descargar audios ------------
def audio():
    import os
    link = videos.get()
    yt = YouTube(link)
    yt = yt.streams.get_audio_only()
    yt.download()
    print("Descarga con éxito")

def audio_playlist():
    import os
    print("Comenzando")
    #Escribir playlist a descargar
    link = videos.get()
    playlist=Playlist(link)
    for video in playlist.videos:
        url=video.watch_url
        yt = pytube.YouTube(url)
        stream = yt.streams.get_audio_only()
        filename = stream.download()
        print("Audio descargado como ", filename)
    print("Playlist descargada")

#----------- Convertirdores ------------
def mp4():
    from pathlib import Path
    carpeta= Path('converter')
    for c in list (carpeta.iterdir()):
        if c.suffix == ".mp4":
            nueva_extension = c.with_suffix(".mp3")
            c.rename(nueva_extension)
    print("Extensión cambiada")

def m4a():
    from pathlib import Path
    carpeta= Path('converter')
    for c in list (carpeta.iterdir()):
        if c.suffix == ".m4a":
            nueva_extension = c.with_suffix(".mp3")
            c.rename(nueva_extension)
    print("Extensión cambiada")

def popup():
    Messagebox.showinfo("Holi","Yo hice esto")

root = Tk()
root.config(bd=15)
root.title("Multi-Media-Tools")

img = Image.open("alex.png")
resized_img = img.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_img)
#image = PhotoImage(file="batma.png")
foto = Label(root, image=photo, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label = "Para más información", menu=helpmenu)
helpmenu.add_command(label = "Información del autor", command=popup)
menubar.add_command(label = "Salir", command=root.destroy)

instrucciones = Label(root,text = "Programa Multi-Media-Tools")
instrucciones.grid(row=1, column=0)

videos = Entry(root)
videos.grid(row=2, column=0)

boton = Button(root, text="Descargar Video", command = video)
boton.grid(row=3, column=0)
boton2= Button(root, text="Playlist de Videos", command = video_playlist)
boton2.grid(row=4, column=0)
boton3 = Button(root, text="Descargar Audio", command = audio)
boton3.grid(row=5, column=0)
boton4= Button(root, text="Playlist de Audios", command = audio_playlist)
boton4.grid(row=6, column=0)
boton5= Button(root, text="De MP4 - MP3 ", command = mp4)
boton5.grid(row=7, column=0)
boton6= Button(root, text="De M4A - MP3", command = m4a)
boton6.grid(row=8, column=0)

root.mainloop()