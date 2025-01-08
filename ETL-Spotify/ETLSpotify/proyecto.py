import spotipy # type: ignore
from spotipy.oauth2 import SpotifyClientCredentials # type: ignore
import pandas as pd
import pandasql as ps # type: ignore


#EXTRACT
#autentificaciones
client_id = '07690910aceb48d69b0cb59e614103ef'
client_secret = '249e4ab420744dbfb7496ea7d983727d'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


playlists = {
    '0SFXg1GGwQqTQxP6WmhfAB':'Andrea idk'
    #'6vHhQOHGABPPMcLumvTBpN':'Filippa Borg'
}

tracks_data = []

for playlist_id, user_name in playlists.items():
    resultado = sp.playlist_tracks(playlist_id)
    for i, item in enumerate(resultado['items']):
       posicion = i+1
       if item['track'] is not None:
           nombre= item['track']['name']
           album = item['track']['album']['name']
           popularidad = item['track']['popularity']
           artista=item['track']['artists'][0]['name']
       else:
           nombre= "error"
           album = "error"
           popularidad = "error"
           artista= "error"
       track_info ={
           'Posicion': posicion,
           'Nombre_canción': nombre,
           'Nombre_album': album,
           'Popularidad': popularidad,
           'Nombre_artista':artista,
           'usuario' : user_name
       }
       tracks_data.append(track_info)

df_tracks = pd.DataFrame(tracks_data)
df_tracks = df_tracks.drop_duplicates()
df_tracks = df_tracks[~df_tracks['Nombre_canción'].str.contains('error', case=False, na=False)]
df_tracks.to_csv('tracks_1d.csv', index=False)

#limpieza de datos, eliminar valores repetidos

#QUERY
query =""" 
SELECT * FROM df_tracks
WHERE CAST(Popularidad AS INTEGER) > 50
ORDER BY Popularidad DESC
LIMIT 10;
"""

top10__sql = ps.sqldf(query,locals())
print(top10__sql)