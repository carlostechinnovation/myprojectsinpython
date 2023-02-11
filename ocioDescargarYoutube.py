#Descarga de videos de Youtube (OCIO) con librería Pytube
from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PL0uH5v2iPsYLYdo-1Egm8UK9YBmCibPCz')
print("Descargando lista de Youtube: " + p.title)

for video in p.videos:
    print("Descargando...:" + video.title)
    video.streams.filter(only_audio=True).first().download(output_path="D:\\misaudios\\")


