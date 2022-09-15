import requests

#headers = {
#    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
#}
#call = requests.get('https://api.openrouteservice.org/geocode/search?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&text=Mouen', headers=headers)

#print(call.status_code, call.reason)
#print(call.text)


#call = requests.get('https://api.openrouteservice.org/geocode/search?api_key=5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab&text=Grenoble', headers=headers)

#print(call.status_code, call.reason)
#print(call.text)


body = {"coordinates":[[8.681495,49.41461],[8.686507,49.41943],[8.687872,49.420318]]}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf6248fb5ed77adb0d4650a8daae0878b1a6ab',
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post('https://api.openrouteservice.org/v2/directions/driving-car', json=body, headers=headers)

print(call.text)