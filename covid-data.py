import requests
import json

response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations')

country = "United Kingdom"
data = response.json()

#print(data["locations"][0])
world_stats = data["latest"]

loc_data = data["locations"]

country_data = []

for location in loc_data:
    #print(location["country"] + " " + str(location["coordinates"]))
    
