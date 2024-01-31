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

#----------- Convertirdores ------------
def mp4():
    from tkinter import Tk
    import tkinter.filedialog as tkf
    import moviepy.editor as editor
    import os

    root = Tk()
    root.withdraw()

    rutas = tkf.askopenfilenames(filetypes=[('Archivos mp4', '*.mp4')])
    for ruta in rutas:
        nombre = os.path.basename(ruta)
        video_clip = editor.VideoFileClip(ruta)
        video_clip.audio.write_audiofile(nombre.replace('.mp4','.mp3'))
import os

#----------- Automatización ------------
def eliminar_videos():
    for archivo in os.listdir():
        if archivo.endswith(".mp4"):
            os.remove(os.path.join(archivo))


def popup():
    Messagebox.showinfo("Holi","Yo hice esto")

root = Tk()
root.config(bd=15)
root.title("Multi-Media-Tools")

#img = Image.open("alex.png")
#resized_img = img.resize((200, 200), Image.ANTIALIAS)
#photo = ImageTk.PhotoImage(resized_img)
#image = PhotoImage(file="batma.png")
#foto = Label(root, image=photo, bd=0)
#foto.grid(row=0, column=0)

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
boton3 = Button(root, text="De MP4 - MP3 ", command = mp4)
boton3.grid(row=5, column=0)
boton4 = Button(root, text="Eliminar videos ", command = eliminar_videos)
boton4.grid(row=6, column=0)

root.mainloop()