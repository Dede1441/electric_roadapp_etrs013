import requests


def list_bornes(waypoint):
    url = f"https://odre.opendatasoft.com/api/records/1.0/search/?dataset=bornes-irve&q=&rows=1&sort=-dist&facet=region&facet=departement&geofilter.distance={waypoint[1]},{waypoint[0]},+100000"
    headers = {     "Content-type": "application/x-www-form-urlencoded",    "Host": "odre.opendatasoft.com",    }

    request = requests.get(url, headers)

    charging_station_service = request.json()

    return charging_station_service["records"][0]["fields"]["geo_point_borne"]
