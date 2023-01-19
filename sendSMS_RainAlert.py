# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:29:38 2023

@author: Dean321
"""
import requests
from twilio.rest import Client

twilio_phoneNumber = "<TWILIO_NUMBER>"
account_sid = "<YOUR_TWILIO_SID>"
auth_token ="<YOUR_TWILIO_TOKEN>"
client = Client(account_sid, auth_token)

api = <OPEN_WEATHER_API_KEY>
lat = <YOUR_LATITUDE>
long = <YOUR_LONGITUDE>
OWM_Endpoint="https://api.openweathermap.org/data/2.5/onecall"
weather_param = {
    "lat":lat,
    "lon":long,
    "appid":api,
    "exclude":"current, minutely, daily"
}

response = requests.get(OWM_Endpoint, params=weather_param)
response.raise_for_status()
weather_data = response.json()
first_12_items = weather_data["hourly"][:12]
carry_umbrella = False
for i in first_12_items:
    for j in i["weather"]:
        if j["id"] <= 700:
            carry_umbrella = True
            break
    if carry_umbrella:
        break
    
if carry_umbrella:
    message = client.messages.create(
      body = "Carry your Umbrella my dear!!!",
      from_ = twilio_phoneNumber,
      to = "<YOUR_NUMBER>"
    )
    print(message.sid)  
else:
    print("You're good for the day!")

          
