# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:10:33 2024

@author: Dean321
"""

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")
tbody = soup.select("table") #all tables
toc = tbody[2] #table of contents
all_tr = toc.select("tr")[:-3]

data = {}
for i in range(0,len(all_tr),3):
    rank = int(all_tr[i].find(name="span",class_="rank").getText()[:-1])
    title = all_tr[i].find(name="span",class_='titleline').a.getText()
    url = all_tr[i].find(name="span",class_='titleline').a.get("href")
    try:
        score = int(all_tr[i+1].find(name="span",class_="score").getText()[:-7])
    except:
        score = 0
    try:
        age = all_tr[i+1].find(name="span", class_="age").getText()
    except:
        print(all_tr[i])
        
    try:
        noc = int(all_tr[i+1].find_all(name="a")[-1].getText()[:-9])
    except:
        noc = 0
        
    data.update({rank:{
        "title":title,
        "url":url,
        "score":score,
        "age":age,
        "noc":noc
        }})

