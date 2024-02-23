from pytube import YouTube
from pytube import *
import pytube
from tkinter import *
from tkinter import messagebox as Messagebox
from PIL import Image, ImageTk
import os
import shutil

#-------- Descargar videos -----------
def video():
    try: 
        link = videos.get()
        yt = YouTube(link)
        yt = yt.streams.get_highest_resolution()
        yt.download()
        Messagebox.showinfo("Holi","Video descargado")
    except:
        Messagebox.showinfo("Holi","Error al descargar video")

def video_playlist():
    link = videos.get()
    playlist=Playlist(link)
    print(playlist)
    for video in playlist.videos:
        try:
            url=video.watch_url
            yt = pytube.YouTube(url)
            stream = yt.streams.get_highest_resolution()
            filename = stream.download()
            print("Video descargado como ", filename)

        except pytube.exceptions.AgeRestrictedError:
            Messagebox.showinfo("Holi",f"El video: {filename}, tiene restricción de edad")
        except pytube.VideoUnavailable:
            Messagebox.showinfo("Holi",f"El video: {filename}, ya no esta disponible")

    Messagebox.showinfo("Holi","Playlist descargada")

#----------- Convertirdores ------------
def mp4():
    from tkinter import Tk
    import tkinter.filedialog as tkf
    import moviepy.editor as editor

    root = Tk()
    root.withdraw()

    rutas = tkf.askopenfilenames(filetypes=[('Archivos mp4', '*.mp4')])
    for ruta in rutas:
        nombre = os.path.basename(ruta)
        video_clip = editor.VideoFileClip(ruta)
        video_clip.audio.write_audiofile(nombre.replace('.mp4','.mp3'))

    Messagebox.showinfo("Holi","Canciones convertidas")

def eliminar_videos():
    for archivo in os.listdir():
        if archivo.endswith(".mp4"):
            os.remove(os.path.join(archivo))
    Messagebox.showinfo("Holi","Videos eliminados")

def mover_canciones():
    carpeta_origen = os.getcwd()
    carpeta_destino = os.path.join(carpeta_origen, "Canciones")
    
    if not os.path.exists(carpeta_destino):
        os.mkdir(carpeta_destino)
        for archivo in os.listdir(carpeta_origen):
            if archivo.endswith(".mp3"):
                shutil.move(os.path.join(carpeta_origen, archivo), os.path.join(carpeta_destino, archivo))
    else:
        for archivo in os.listdir(carpeta_origen):
            if archivo.endswith(".mp3"):
                shutil.move(os.path.join(carpeta_origen, archivo), os.path.join(carpeta_destino, archivo))
    Messagebox.showinfo("Holi","Canciones movidas")

def popup():
    Messagebox.showinfo("Holi","Yo hice esto")

root = Tk()
root.config(bd=15)
root.title("Multi-Media-Tools")

img = Image.open("alex.png")
resized_img = img.resize((200, 200))
photo = ImageTk.PhotoImage(resized_img)
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
boton3 = Button(root, text="De MP4 - MP3 ", command = mp4)
boton3.grid(row=5, column=0)
boton4 = Button(root, text="Eliminar videos ", command = eliminar_videos)
boton4.grid(row=6, column=0)
boton5 = Button(root, text="Mover canciones ", command = mover_canciones)
boton5.grid(row=7, column=0)

root.mainloop()