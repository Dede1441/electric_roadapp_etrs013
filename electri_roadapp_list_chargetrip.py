import requests
import json
import pandas as pd

def list_from_chargetrip(search) :
    headers = {
        "x-client-id": '634d6831d0930830249a0855',
        "x-app-id": '634d6831d0930830249a0857'
    }
    url = 'https://api.chargetrip.io/graphql'
    query = """
        query carListAll {
            carList (size: 15, search: "{search}"){
                id
                naming {
                    make
                    model
                    version
                    edition
                    chargetrip_version
                }
                range {
                    chargetrip_range {
                        best
                        worst
                    }
                }
            }
        }
    """.replace("{search}", search)

    r = requests.post(url=url, json={'query': query}, headers=headers).json()
    all_vehicules=[]

    for vehicules in r['data']['carList'] :
        make = vehicules['naming']['make']
        model = vehicules['naming']['model']
        version =  vehicules['naming']['version']
        if version == None :
            version = ''
        range = (vehicules['range']['chargetrip_range']['best'] + vehicules['range']['chargetrip_range']['worst']) / 2
        info = make,model,version,range
        all_vehicules.append(info)
    return(all_vehicules)