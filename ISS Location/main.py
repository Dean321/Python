# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:56:49 2023

@author: Dean321

Error Status Codes

1XX : Hold On
2XX : Here you go
3XX : Go away
4XX : You screwed up
5XX : I screwed up

"""

import requests
from datetime import datetime
import smtplib
import time

my_email = "example@mail.com"
my_pass = "AppPassword"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
response.raise_for_status()

data = response.json()
# print(data)

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
iss_position = [longitude, latitude]
print(iss_position)

response = requests.get(url="https://api.sunrise-sunset.org/json?lat=18.5204000&lng=73.8567000", params={"formatted":0})
# print(response)
response.raise_for_status()

data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# print(sunrise, sunset)

sunrise_time = int(sunrise.split("T")[1].split(":")[0])
sunset_time = int(sunset.split("T")[1].split(":")[0])

print(sunrise_time, sunset_time)

time_now = int(datetime.now().strftime("%H"))
print(time_now)

while True:
    time.sleep(60)
    my_position = [73.8567, 18.5204]
    if ((iss_position[0] > my_position[0] - 50) or (iss_position[0] < my_position[0] + 50) ) and ( (iss_position[1] > my_position[1] - 50) or (iss_position[1] < my_position[1] + 50)):
        if time_now >= sunset or time_now< sunrise:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()# transport layer security
                connection.login(user=my_email, password=my_pass)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs=my_email, 
                    msg='''Subject:ISS here you\n\n
                    LOOK UP'''
                    )
            break