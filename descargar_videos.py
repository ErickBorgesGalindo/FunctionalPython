from pytube import *
import pytube
import os

#Escribir playlist a descargar
playlist=Playlist("https://www.youtube.com/playlist?list=PL3wY3HJjjXVxIfYbOGhdZhuDaavWErdIG")


for video in playlist.videos:
    url=video.watch_url
    yt = pytube.YouTube(url)
    stream = yt.streams.get_lowest_resolution()
    filename = stream.download()
    os.rename(filename, f'{yt.publish_date}_{yt.title}.mp4')
    print("Video descargado como ", filename)
