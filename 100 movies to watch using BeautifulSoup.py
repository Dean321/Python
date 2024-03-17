# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:27:45 2024

@author: Dean321
"""

from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")
title_box = soup.find_all(name="div",class_="entity-info-items info-items__collapsed")[0]
movies = title_box.select("li a")
list_of_movies = []
for i in range(0, len(movies)):
    list_of_movies.append(str(i+1)+") "+movies[i].getText())
    
with open("movies.txt","a") as f:
    for i in list_of_movies:
        f.write(i+"\n")

    
