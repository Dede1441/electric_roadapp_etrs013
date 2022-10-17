from unittest import TestLoader
from flask import Flask, render_template, request
import electric_roadapp_client
import electric_roadapp_requests_openmaps
import electric_roadapp_list_chargetrip
import electric_roadapp_list_bornes
import json
import folium
from folium.plugins import MarkerCluster
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Then get the data from the form
        autonomie = request.form['autonomie']
        vehicules=autonomie.split(" ")
        autonomie=vehicules[3]
        ville_a = request.form['ville_a']
        ville_b = request.form['ville_b']
        #distance = request.form['distance']
        vit_moy = request.form['vit_moy']

        if int(vit_moy) <= 0 :
            vit_moy = 120

        geocode_zipa = electric_roadapp_requests_openmaps.getlocation(ville_a)
        geocode_zipb = electric_roadapp_requests_openmaps.getlocation(ville_b)


        distance = electric_roadapp_requests_openmaps.getdistance(geocode_zipa,geocode_zipb)
        print(distance)
        duree_trajet=electric_roadapp_client.duree_trajet(int(distance),vit_moy)

        if float(autonomie) > float(distance) :

            map_center = [0,1]
            map_center[0] = (geocode_zipa[0] + geocode_zipb[0]) / 2
            map_center[1] = (geocode_zipa[1] + geocode_zipb[1]) / 2
            map_center = str(map_center[1]) + ', ' + str(map_center[0])

            geocode_zipa = str(geocode_zipa[1]) + ', ' + str(geocode_zipa[0])
            geocode_zipb = str(geocode_zipb[1]) + ', ' + str(geocode_zipb[0])

            return render_template('trajet.html',duree_trajet=duree_trajet[0],geocode_zipa=geocode_zipa, geocode_zipb=geocode_zipb,map_center=map_center)
        else :
            print('waypoints')
            all_waypoints = ''
            distance_restante = distance
            next_waypoint=electric_roadapp_requests_openmaps.calcul_next_waypoint(geocode_zipa,geocode_zipb,autonomie)
            distance_restante = distance_restante - next_waypoint[1]
            #duree_trajet=electric_roadapp_client.duree_trajet(int(distance),vit_moy)
            while float(distance_restante) > float(autonomie) :
                #intérogation autour de str(next_waypoint[0][1]) + ", " + str(next_waypoint[0][0])
                borne_waypoint=electric_roadapp_list_bornes.list_bornes(next_waypoint[0])
                print(borne_waypoint)
                temp_waypoint= "L.latLng(" + str(borne_waypoint[0]) + ", " + str(borne_waypoint[1]) + "),"
                #temp_waypoint prendra ce nouveau point de la station de recharge

                all_waypoints= all_waypoints + temp_waypoint

                #A voir comment distance restante se comporte, on sera pas trop loin de la realite de toute façon + on a cheat pour les petites autonomies
               
                #il faudra feed la fonction par les novuelles coordonnées
                borne_waypoint=list(reversed(borne_waypoint))
                next_waypoint=electric_roadapp_requests_openmaps.calcul_next_waypoint(borne_waypoint,geocode_zipb,autonomie)
                distance_restante = distance_restante - next_waypoint[1]

            map_center = [0,1]
            map_center[0] = (geocode_zipa[0] + geocode_zipb[0]) / 2
            map_center[1] = (geocode_zipa[1] + geocode_zipb[1]) / 2
            map_center = str(map_center[1]) + ', ' + str(map_center[0])
            geocode_zipa = str(geocode_zipa[1]) + ', ' + str(geocode_zipa[0])
            geocode_zipb = str(geocode_zipb[1]) + ', ' + str(geocode_zipb[0])

            return render_template('trajet_charge.html',duree_trajet=duree_trajet[0],geocode_zipa=geocode_zipa, geocode_zipb=geocode_zipb,map_center=map_center,all_waypoints=all_waypoints) #ne pas oublier l'envoi du tableau + trajet

    else:  
        args = request.args
        search = args.get("search",default="Tesla")
    
        list_vehicules_detailed=electric_roadapp_list_chargetrip.list_from_chargetrip(search)
        list_vehicules = []
        for vehicules in list_vehicules_detailed :
            vehicule=vehicules[0].replace(' ', '-') + ' ' + vehicules[1].replace(' ', '-') + ' ' + vehicules[2].replace(' ', '') + ' ' + str(vehicules[3]).replace(' ', '-')
            list_vehicules.append(vehicule)
        return render_template('index.html',list_vehicules=list_vehicules)