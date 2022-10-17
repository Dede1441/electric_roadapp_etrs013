from ast import Try
from math import dist
import requests
import json

def getlocation(zipcode) :
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    url = "https://api.openrouteservice.org/geocode/search?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&text=" + str(zipcode) + "&boundary.country=FR"
    call = requests.get(url ,headers=headers)
    location=json.loads(call.text)
    geo_location=location["features"][0]["geometry"]["coordinates"]
    return(geo_location)

def getdistance(ville_a, ville_b) :
    import requests

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    ville_a = str(ville_a[0]) + ',' + str(ville_a[1])
    ville_b = str(ville_b[0]) + ',' + str(ville_b[1])
    url = "https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&start=" + str(ville_a) + "&end=" + str(ville_b)
    call = requests.get( url, headers=headers)
    distance=(call.json()['features'][0]['properties']['segments'][0]['distance'])*0.001
    return (distance)

def getpath(ville_a, ville_b) :
    import requests

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    ville_a = str(ville_a[0]) + ',' + str(ville_a[1])
    ville_b = str(ville_b[0]) + ',' + str(ville_b[1])
    url = "https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&start=" + str(ville_a) + "&end=" + str(ville_b)
    call = requests.get( url, headers=headers)

    return (call.text)


def calcul_next_waypoint(waypoint_a, waypoint_b, autonomie):
    waypoint_a = str(waypoint_a[0]) + ',' + str(waypoint_a[1])
    waypoint_b = str(waypoint_b[0]) + ',' + str(waypoint_b[1])
    headers = { 'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8', }
    distance_tempo = 0
    call = requests.get('https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&start=' + str(waypoint_a) + '&end=' + str(waypoint_b), headers=headers)
    compteur=0
    compteur_max=0
    for step in (call.json()['features'][0]['properties']['segments'][0]['steps']) :
        compteur_max +=1

    while True :
        

        geo_location_distance=(call.json()['features'][0]['properties']['segments'][0]['steps'][compteur]['distance'])*0.001

        #incrémenter pour récupérer le prochain segment (addition des segments)
        distance_tempo = distance_tempo + geo_location_distance
 
        #incrémenter pour calculer entre les waypoints
        compteur += 1

        if int(distance_tempo) > int(autonomie) :
            compteur = compteur - 1
            distance_tempo = distance_tempo - geo_location_distance
            break
            
        if compteur == compteur_max :
            break

    waypoint_end=call.json()['features'][0]['geometry']['coordinates'][compteur]

    return(waypoint_end,distance_tempo)

