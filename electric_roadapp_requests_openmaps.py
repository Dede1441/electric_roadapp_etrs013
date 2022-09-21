import requests
import json

def getlocation(zipcode) :
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    url = "https://api.openrouteservice.org/geocode/search?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&text=" + str(zipcode) + "&boundary.country=FR"
    call = requests.get(url ,headers=headers)
    
    print(call.status_code, call.reason)
    return(call.text)


def getpath(ville_a, ville_b) :
    import requests

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    url = "https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&start=" + str(ville_a) + "&end=" + str(ville_b)
    call = requests.get( url, headers=headers)
    return (call.text)

