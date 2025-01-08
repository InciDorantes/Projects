#instalar pandas
#instalar spotipy

import spotipy # type: ignore
from spotipy.oauth2 import SpotifyClientCredentials # type: ignore
import pandas as pd

#EXTRACT
#autentificaciones
client_id = '07690910aceb48d69b0cb59e614103ef'
client_secret = '249e4ab420744dbfb7496ea7d983727d'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

nombre_artista = 'One Direction'
resultado = sp.search(q = 'artist:' + nombre_artista, type ='artist') 

#TRANSFORM
#Limpiando datos
artistas = resultado['artists']['items']

lista_artistas = []

for artista in artistas:
    nombre = artista['name']
    popularidad = artista['popularity']
    seguidores = artista['followers']['total']
    lista_artistas.append([nombre, popularidad, seguidores])

#creamos data frame
df_artistas = pd.DataFrame(lista_artistas, columns=['nombre', 'popularidad','seguidores'])

#print(df_artistas)
#'6vHhQOHGABPPMcLumvTBpN'
playlist_id = '0SFXg1GGwQqTQxP6WmhfAB'
resultado = sp.playlist_tracks(playlist_id, market=None)

print(resultado)