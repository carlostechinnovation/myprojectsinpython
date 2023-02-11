"""
Descarga de audios/videos de Youtube (OCIO) con librería Pytube
"""
from pytube import Playlist

print("===== INICIO =====")

PARAM_MODO="SOLO_AUDIO"         # SOLO_AUDIO, AUDIO_Y_VIDEO
PARAM_PATH_DIRECTORIO="D:\\"    # Directorio local donde se descarga

print("PARAM_MODO=" + PARAM_MODO)
print("PARAM_PATH_DIRECTORIO=" + PARAM_PATH_DIRECTORIO)

############ FUNCION PROCESAR LISTA #################
def procesarPlaylist(playlistUrl, modo):
    p=Playlist(url=playlistUrl)
    print("---------------------- Descargando LISTA de Youtube llamada: " + str(p.title) +" ("+playlistUrl+") "+"----------------------")
    carpeta=str(p.title).replace(" ", "_")
    pathCarpeta="D:\\"+carpeta+"\\"
    
    for video in p.videos:
        print("Descargando...:" + video.title)
        if (modo == "SOLO_AUDIO"):
            video.streams.filter(only_audio=True).first().download(output_path=pathCarpeta)
        elif (modo == "SOLO_AUDIO"):
            video.streams.first().download(output_path=pathCarpeta)
        else:
            print("ERROR: el MODO es incorrecto. Revisar. Saliendo...")
            #exit()
    

################ MAIN #########################

#Lista de playlists de Youtube
misPlaylists=[#'https://www.youtube.com/playlist?list=PL0uH5v2iPsYLYdo-1Egm8UK9YBmCibPCz',
              'https://www.youtube.com/playlist?list=PLD4932A345F3C12CA',
              'https://www.youtube.com/playlist?list=PL0uH5v2iPsYIn8o2huo7_kjiaF9sAPsBm',
              'https://www.youtube.com/playlist?list=PLFEC727ABF3D001A3',
              'https://www.youtube.com/playlist?list=PL0uH5v2iPsYKP72T5uybzlLfzM-g6RIwJ',
              'https://www.youtube.com/playlist?list=PL0uH5v2iPsYKxnOQQAb91JgzyBUGBdVXM',
              'https://www.youtube.com/playlist?list=PL0uH5v2iPsYKh4AII2FrBgNjx8hJUILGS',
              'https://www.youtube.com/playlist?list=PLF118EB4DC828CD43',
              'https://www.youtube.com/playlist?list=PLSXGfg6XHVB4O1unWMJIyfL2FTgC0maOo',
              'https://www.youtube.com/playlist?list=PLKdyCI0t8hb8jC8gsub39H7pVQ5FKMllD']

print("Se van a descargar " + str(len(misPlaylists)) + " listas de Youtube.")

for p in misPlaylists:
    procesarPlaylist(playlistUrl=p, modo=PARAM_MODO)

print("===== FIN =====")
