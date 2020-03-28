import requests
import json

response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations')

country = "United Kingdom"
data = response.json()

#print(data["locations"][0])
world_stats = data["latest"]

loc_data = data["locations"]

confirmed_data = []
death_data = []

for location in loc_data:
    #print(location["country"] + " " + str(location["coordinates"]))
    if(country == location["country"]):
        confirmed_data.append(location["latest"]["confirmed"])
        death_data.append(location["latest"]["deaths"])

confirmed = sum(confirmed_data)
deaths = sum(death_data)

print(confirmed)
print(deaths)