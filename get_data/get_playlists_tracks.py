import spotipy
import json
from datetime import date

cred = spotipy.SpotifyClientCredentials(client_id="3d6d83f030744a4b8065ffef99420660", client_secret="7576c44b974448c884702e4e316825ff")

sp = spotipy.Spotify(client_credentials_manager=cred)

countries_list = ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC',
                  'SV', 'EE', 'FI', 'FR', 'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI',
                  'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG',
                  'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']

i = 0

today = date.today().strftime("%Y%m%d")

file = 'rawdata/playlists/{}.txt'.format(today)

with open(file, "w") as f:
    for country in countries_list:
        play = [(pl['name'], pl['id']) for pl in sp.category_playlists("toplists", country)['playlists']['items']]
        for p in play:
            playlist = sp.playlist(p[1])
            track_list = [track['track'] for track in playlist['tracks']['items'] if track['track'] is not None]
            for track in track_list:
                track['playlist'] = {
                    "playlist_id": playlist['id'],
                    "playlist_name": playlist['name'],
                    "playlist_url": playlist['external_urls'],
                    "playlist_country": country
                }
                json.dump(track, f, sort_keys=True)
                f.write('\n')
            i = i + len(track_list)
            print(i)
    f.close()