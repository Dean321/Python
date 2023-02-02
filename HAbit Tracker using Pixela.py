# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:33:38 2023

@author: Dean321
"""
import requests
from datetime import datetime
from datetime import date

TODAY = datetime.now().strftime("%Y%m%d")
USERNAME = <your_user_id>
TOKEN = <your_madeup_token>
GRAPH_ID = <your_graph_id>
PIXELA_ENDPOINT = "https://pixe.la//v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
UPDATE_PIXEL_ENDPOINT = f"{PIXEL_ENDPOINT}/{TODAY}"

headers = {
    "X-USER-TOKEN":TOKEN
}

Created a user it's a one-time activity
user_params={
    "token":USERNAME,
    "username":TOKEN,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response)

Creating your graph
graph_config = {
    "id": "graph1",
    "name":"Cycling Graph",
    "unit": "Km",
    "type":"float",
    "color":"ajisai"
        
}
grap_response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(grap_response)

Putting a pixel n the graph
pixel_congif = {
    "date":TODAY,
    "quantity":"3"    
}
pixel_response = requests.post(url=PIXEL_ENDPOINT, json=pixel_congif, headers=headers)
print(pixel_response)

Formate date example
today = datetime.now().strftime("%Y%m%d")
print(today)

Updating pixel
update_pixel_config = {
    "quantity":"9"    
}
print(UPDATE_PIXEL_ENDPOINT)
update_pixel_response = requests.put(url=UPDATE_PIXEL_ENDPOINT, 
                                      json=update_pixel_config, 
                                      headers=headers)
print(update_pixel_response)

deleting a pixel
delete_pixel_response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)
print(delete_pixel_response)




