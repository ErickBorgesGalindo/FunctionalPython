opcion = ""

while opcion !="6":
    print("Bienvenido, por favor selecciona una opción: ")
    print("1. Descargar video.")
    print("2. Descargar muchos videos.")
    print("3. Descargar audio.")
    print("4. Descargar muchos audios.")
    print("5. Cambiar extensión.")
    print("6. Salir del programa.")
    opcion = input("Ingresa tu opcion: ")

    if(opcion == "1"):
        from pytube import YouTube
        import os
        def Download(link):
            yt = YouTube(link)
            yt = yt.streams.get_highest_resolution()
            try :
                yt.download()
            except :
                print("Hubo un error")
            print("Descarga con éxito")

        link = input("Ingresa tu link: ")
        Download(link)

    if(opcion == "2"):
        from pytube import *
        import pytube
        import os

        #Escribir playlist a descargar
        link = input("Ingresa tu link: ")
        playlist=Playlist(link)
        for video in playlist.videos:
            video.streams.first().download()
            #url=video.watch_url
            #yt = pytube.YouTube(url)
            #stream = yt.streams.get_highest_resolution()
            #filename = stream.download()
            #print("Video descargado como ", filename)

    if(opcion == "3"):
        from pytube import YouTube
        import os
        def Download(link):
            yt = YouTube(link)
            yt = yt.streams.get_audio_only()
            try :
                yt.download()
            except :
                print("Hubo un error")
            print("Descarga con éxito")

        link = input("Ingresa tu link: ")
        Download(link)

    if(opcion == "4"):
        from pytube import *
        import pytube
        import os

        #Escribir playlist a descargar
        link = input("Ingresa tu link: ")
        playlist=Playlist(link)
        for video in playlist.videos:
            url=video.watch_url
            yt = pytube.YouTube(url)
            stream = yt.streams.get_audio_only()
            filename = stream.download()
            print("Video descargado como ", filename)
    if(opcion == "5"):
        from pathlib import Path
        carpeta= Path('converter')
        for c in list (carpeta.iterdir()):
            if c.suffix == ".m4a":
                nueva_extension = c.with_suffix(".mp3")
                c.rename(nueva_extension)