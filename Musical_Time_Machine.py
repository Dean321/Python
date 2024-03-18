# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:51:47 2024

@author: Dean321
"""

from bs4 import BeautifulSoup
import requests

# Billboards top 100 songs
url = "https://www.billboard.com/charts/hot-100/"
# get desired date
dd = input("Enter your date in this format YYYY-MM-DD - ")
updated_url = url +dd
print(updated_url)
response = requests.get(updated_url)
soup = BeautifulSoup(response.text, "html.parser")

boxes = soup.select("div .o-chart-results-list-row-container")
data = {}
cnt = 0
for box in boxes:
    cnt+=1
    text_box = box.find_all(name="li",class_="o-chart-results-list__item")
    title = text_box[3].find(name="h3",class_="c-title").getText().strip()
    artist = text_box[3].find(name="span",class_="c-label").getText().strip()
    data.update({cnt:{"title":title, "artist":artist}})
# print(len(data), cnt)

Spotify_Client_ID = ""
Spotify_client_secret = ""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

sp =  spotipy.Spotify(
auth_manager=SpotifyOAuth(
scope="playlist-modify-private",
redirect_uri="http://example.com",
client_id=Spotify_Client_ID,
client_secret=Spotify_client_secret,
show_dialog=True,
cache_path="token.txt"
)
)
User_id = sp.current_user()["id"]
# example: https://example.com/?code=
# spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=Spotify_Client_ID,
                                                           # client_secret=Spotify_client_secret))

# results = sp.search(q='lover', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

songs = []
for i in data:
    name = data[i]["artist"].split()[0]
    title= data[i]["title"]
    travel_date = dd.split('-')[0]
    # results = sp.search(q=title, limit=1)
    # sp.search(q='artist:' + name, type='artist')
    # items = results['artists']['items']
    # item = results["tracks"]["items"][0]
    result = sp.search(q=f"track:{title} year:{travel_date}", type="track")
    uri = result["tracks"]["items"][0]["uri"]
    songs.append(uri)
    # break		

top_100 = sp.user_playlist_create(
    user=User_id, 
    name=f"{travel_date} Billboard 100", 
    public=False)
sp.playlist_add_items(
    playlist_id=top_100["id"], 
    items=songs)