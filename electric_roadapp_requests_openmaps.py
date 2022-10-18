from ast import Try
from math import dist
import requests
import json
#import time

def getaddress(waypoints) :
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    url = "https://api.openrouteservice.org/geocode/reverse?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&point.lon=" + str(waypoints[0]) + "&point.lat=" + str(waypoints[1]) +"&layers=address&boundary.country=FR"
    call = requests.get(url ,headers=headers)
    location=json.loads(call.text)
    try:
        address=location["features"][0]["properties"]["label"]
    except :
        address=waypoints
    return(address)


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
    #time.sleep(1)
    compteur=0
    compteur_max=0
    distance_tempo02 = {}
    for step in (call.json()['features'][0]['properties']['segments'][0]['steps']) :
        compteur_max +=1
    #Tentative de régler le problème de d'autonomie sur les longs segments tout en évitant la panne sèche
    #max_segment_size={}
    #for step in (call.json()['features'][0]['properties']['segments'][0]['steps']) :
    #    max_segment_size.append(call.json()['features'][0]['properties']['segments'][0]['steps'][1]['distance'])
    #    max_segment_size=max(max_segment_size)
    #    compteur+=1
    #Il suffirait de récuperer les segments trop gros et de les découper, puisqu'on as les waypoints dans les segments dans la réponse de openstreetmap. 

    compteur=0
    while True :
        
        geo_location_distance=(call.json()['features'][0]['properties']['segments'][0]['steps'][compteur]['distance'])*0.001

        #incrémenter pour récupérer le prochain segment (addition des segments)
        distance_tempo = distance_tempo + geo_location_distance
        distance_tempo02[compteur] = distance_tempo
        #incrémenter pour calculer entre les waypoints
        compteur += 1
        #Tentative de régler le problème de d'autonomie sur les longs segments tout en évitant la panne sèche
        #if float(distance_tempo) > 2*(float(autonomie)) :
        #    autonomie += 100 #Cheat_code pour surpasser le probleme d'autoroute + longue que l'autonomie. Avec les segments il serait possibles d'overcome ce problème
        #    break
        if compteur == compteur_max :
            compteur -= 1
            break
        #print('distance_tempo=',distance_tempo,'autonomie=',autonomie)
        if float(distance_tempo) > float(autonomie) :

            #Eviter d'arriver en panne seche. Problème : si l'autonomie est plus petites que les segments, ça boucle. Tentatives de résolution plus hauts
            #compteur -= 1
            #distance_tempo = distance_tempo - geo_location_distance

            break
            
    last_waypoint_step=call.json()['features'][0]['properties']['segments'][0]['steps'][compteur]['way_points'][1]
    waypoint_end=call.json()['features'][0]['geometry']['coordinates'][last_waypoint_step]
 

    return(waypoint_end,distance_tempo)

