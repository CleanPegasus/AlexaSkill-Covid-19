import requests
import json


def world_data():
    response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations')
    data = response.json()
    return data["latest"]["confirmed"], data["latest"]["deaths"]

def country_data(country):
    response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations')
    data = response.json()
    loc_data = data["locations"]
    confirmed_data = []
    death_data = []

    for location in loc_data:
        #print(location["country"] + " " + str(location["coordinates"]))
        if(country == location["country"]):
            confirmed_data.append(location["latest"]["confirmed"])
            death_data.append(location["latest"]["deaths"])
            
    return sum(confirmed_data), sum(death_data)