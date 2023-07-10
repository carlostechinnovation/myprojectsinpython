"""
Descarga de audios/videos de Youtube (OCIO) con librería Pytube
"""
from pytube import Playlist  # https://pytube.io/en/latest/index.html
from datetime import datetime


PARAM_MODO = "SOLO_AUDIO"         # SOLO_AUDIO, AUDIO_Y_VIDEO
PARAM_PATH_DIRECTORIO = "C:\\DATOS\\MUSICA_YOUTUBE\\"    # Directorio local donde se descarga

print("PARAM_MODO=" + PARAM_MODO)
print("PARAM_PATH_DIRECTORIO=" + PARAM_PATH_DIRECTORIO)

############ FUNCION PROCESAR LISTA #################


def procesarPlaylist(playlistUrl, modo):
    """FUNCION PROCESAR LISTA

    Args:
        playlistUrl (_type_): URL de la playlist
        modo (_type_): Modo de descarga: SOLO_AUDIO, AUDIO_Y_VIDEO
    """
    p = Playlist(url=playlistUrl)

    nombrePlaylist = p.title
    characters_to_remove = ",<>:\"/\\|?*#"
    for character in characters_to_remove:
        nombrePlaylist = nombrePlaylist.replace(character, "")

    print("---------------------- Descargando LISTA de Youtube llamada: " +
          str(nombrePlaylist) + " ("+playlistUrl+") "+"----------------------")
    pathCarpeta = "D:\\"+nombrePlaylist+"\\"
    contador = 0

    for video in p.videos:
        contador += 1
        tituloFichero = "video_"+str(contador)+".mp4"  # default
        try:
            tituloFichero = video.title

            # Caracteres reservados en Windows:
            # https://stackoverflow.com/questions/50365006/is-it-possible-to-ensure-a-filename-or-path-is-windows-legal-using-python
            characters_to_remove = ",<>:\"/\\|?*#"
            for character in characters_to_remove:
                tituloFichero = tituloFichero.replace(character, "")

            tituloFichero = tituloFichero[0:100]  # substring sin extension
        except:
            print("ERROR al extraer el nombre del video. Se pone un nombre por defecto")

        print("Descargando: " + tituloFichero)
        if (modo == "SOLO_AUDIO"):
            video.streams.filter(only_audio=True).first().download(
                output_path=pathCarpeta, filename=tituloFichero+".mp3", skip_existing=True, max_retries=2)
        elif (modo == "AUDIO_Y_VIDEO"):
            video.streams.first().download(output_path=pathCarpeta,
                                           filename=tituloFichero+".mp4", skip_existing=True, max_retries=2)
        else:
            print("ERROR: el MODO es incorrecto. Revisar. Saliendo...")
            # exit()


################ MAIN #########################
if __name__ == '__main__':

    print("===== INICIO =====")

    # Lista de playlists de Youtube
    misPlaylists = [  # 'https://www.youtube.com/playlist?list=PL0uH5v2iPsYLYdo-1Egm8UK9YBmCibPCz',
         'https://www.youtube.com/playlist?list=PLD4932A345F3C12CA',
        # 'https://www.youtube.com/playlist?list=PL0uH5v2iPsYIn8o2huo7_kjiaF9sAPsBm',
        # 'https://www.youtube.com/playlist?list=PLFEC727ABF3D001A3',
        # 'https://www.youtube.com/playlist?list=PL0uH5v2iPsYKP72T5uybzlLfzM-g6RIwJ',
        # 'https://www.youtube.com/playlist?list=PL0uH5v2iPsYKxnOQQAb91JgzyBUGBdVXM',
        # 'https://www.youtube.com/playlist?list=PL0uH5v2iPsYKh4AII2FrBgNjx8hJUILGS',
        # 'https://www.youtube.com/playlist?list=PLF118EB4DC828CD43',
        # 'https://www.youtube.com/playlist?list=PLSXGfg6XHVB4O1unWMJIyfL2FTgC0maOo',
        # 'https://www.youtube.com/playlist?list=PLKdyCI0t8hb8jC8gsub39H7pVQ5FKMllD'
    ]

    print("Se van a descargar " + str(len(misPlaylists)) + " listas de Youtube.")

    for p in misPlaylists:
        procesarPlaylist(playlistUrl=p, modo=PARAM_MODO)

    print("===== FIN =====")
