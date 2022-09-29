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


def getpath(ville_a, ville_b) :
    import requests

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    url = "https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&start=" + str(ville_a) + "&end=" + str(ville_b)
    call = requests.get( url, headers=headers)
    return (call.text)


def calcul_next_waypoint(waypoint_a, waypoint_b, autonomie):
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    distance = 0
    call = requests.get('https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&start=' + str(waypoint_a) + '&end=' + str(waypoint_b), headers=headers)
    
    while distance < autonomie :
        geo_location_distance=location["bbox"]["properties"]["segments"]["distance"]
        #incrémenter pour récupérer le prochain segment -> 
        #incrémenter pour calculer entre les waypoints
        distance = distance + geo_location_distance

    waypoint_end=geo_waypoint_distance=location["bbox"]["properties"]["segments"]["distance"]

    return(waypoint_end)
#boucle Calcul depuis direction pour recuperer waypoint de autonomie max pour envoie api borne (radius)


#Recuperation waypoint borne de recharge -> reprise du calcul depuis nouveau waypoint 
pointa = getlocation(14790)
pointb = getlocation(73000)
calcul_next_waypoint(pointa,pointb,200)