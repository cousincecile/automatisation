import spotipy
import json
from datetime import date

cred = spotipy.SpotifyClientCredentials(client_id='2c5fa0bc4bb5411ba0b5f6d844089b4d', client_secret='fda690d54f1a48f4b8adf2ea88f6b45d')

sp = spotipy.Spotify(client_credentials_manager=cred)

countries_list = ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC',
                  'SV', 'EE', 'FI', 'FR', 'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI',
                  'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG',
                  'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']

today = date.today().strftime("%Y-%m-%d")

file = 'raw_data/playlists/{}.txt'.format(today)

with open(file, "w") as f:
    for country in countries_list:
        play = [(pl['name'], pl['id']) for pl in sp.category_playlists("toplists", country)['playlists']['items']]
        for p in play:
            playlist = sp.playlist(p[1])
            track_list = [track['track'] for track in playlist['tracks']['items'] if track['track'] is not None]
            for track in track_list:
                track['artists'] = track['artists'][0]
                track['playlist'] = {
                    "id": playlist['id'],
                    "name": playlist['name']
                }
                json.dump(track, f, sort_keys=True)
                f.write('\n')
