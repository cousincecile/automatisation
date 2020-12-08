from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint
import json

client_credentials_manager = SpotifyClientCredentials(client_id='2c5fa0bc4bb5411ba0b5f6d844089b4d', client_secret='fda690d54f1a48f4b8adf2ea88f6b45d')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Artist ID de Jul : 3IW7ScrzXmPvZhB27hmfgy
#Artist ID de Nekfeu : 4LXBc13z5EWsc5N32bLxfH
#Artist ID de Petit biscuit : 6gK1Uct5FEdaUWRWpU4Cl2

#Artiste -> liste des albums (ids) -> liste des tracks par albums-> récupérer toutes les popularité associés aux tracks

id_jul = '3IW7ScrzXmPvZhB27hmfgy'
id_nekfeu = '4LXBc13z5EWsc5N32bLxfH'
id_petitb = '6gK1Uct5FEdaUWRWpU4Cl2' 

def get_all_albums_id(id):
    albums_ids = []
    artist_albums = sp.artist_albums(id)
    for item in artist_albums['items']:
        albums_ids.append(item['id'])
    return albums_ids

def get_all_tracks_id(id):
    tracks_ids = []
    tracks_album = sp.album_tracks(id)
    for item in tracks_album['items']:
        tracks_ids.append(item['id'])
    return tracks_ids

def get_all_tracks_with_popularity(ids):
    tracks = []
    for item in ids:
        tracks.append((sp.track(item)))
    return tracks

albums_id = get_all_albums_id(id_nekfeu)
tracks = []
for item in albums_id:
    print("1")
    tracks.append(get_all_tracks_id(item))

track_popularity = []

for item in tracks:
    print("2")
    track_popularity.append(get_all_tracks_with_popularity(item))

file = 'data_popularity.txt'
with open(file, "w") as f:
    json.dump(track_popularity, f, sort_keys=True)


#print(get_all_tracks_with_popularity(get_all_tracks_id('5e5kGSnnDPARPjjrUdGWjf')))
