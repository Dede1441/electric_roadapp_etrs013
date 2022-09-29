from flask import Flask, render_template, request
import electric_roadapp_client
import electric_roadapp_requests_openmaps
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
        ville_a = request.form['ville_a']
        ville_b = request.form['ville_b']
        distance = request.form['distance']
        vit_moy = request.form['vit_moy']
        if autonomie > distance :
            #Calcul de la durée du trajet
            duree_trajet=electric_roadapp_client.duree_trajet(distance,vit_moy)
            #=
            geocode_zipa = electric_roadapp_requests_openmaps.getlocation(ville_a)
            geocode_zipb = electric_roadapp_requests_openmaps.getlocation(ville_b)

            direction_trajet_autonomie_calcul = electric_roadapp_requests_openmaps.getpath(geocode_zipa,geocode_zipb)

            return render_template('trajet.html',duree_trajet=duree_trajet,geocode_zipa=geocode_zipa, geocode_zipb=geocode_zipb)
        else :
            autonomie_manquante = int(distance) - int(autonomie)
            return render_template('notenough.html',autonomie_manquante=autonomie_manquante)

        # Generate just a boring response
        #return 'The cities are %s and %s ' % (ville_a, ville_b) 


    # Otherwise this was a normal GET request
    else:   
        return render_template('index.html')