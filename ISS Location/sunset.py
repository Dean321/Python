# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 18:35:47 2023

@author: Dean321
"""

import requests
from datetime import datetime

response = requests.get(url="https://api.sunrise-sunset.org/json?lat=18.5204000&lng=73.8567000", params={"formatted":0})
# print(response)
response.raise_for_status()

data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise, sunset)

sunrise_time = sunrise.split("T")[1].split(":")[0]
sunset_time = sunset.split("T")[1].split(":")[0]

print(sunrise_time, sunset_time)

time_now = datetime.now()