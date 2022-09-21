from flask import Flask, render_template, request
import electric_roadapp_client
import electric_roadapp_requests_openmaps
import json

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
            zipa = electric_roadapp_requests_openmaps.getlocation(ville_a)
            zipb = electric_roadapp_requests_openmaps.getlocation(ville_b)
            #json_geocode = 
            direction_trajet_calcul = electric_roadapp_requests_openmaps.getpath(zipa,zipb)
            direction_trajet = "https://maps.openrouteservice.org/#/directions/" + str(zipa) +"/" + str(zipb) + "/data/55,130,32,198,15,97,4,224,38,9,96,59,2,24,5,192,166,6,113,0,184,64,90,0,24,3,160,5,128,14,115,8,17,128,54,1,152,1,165,32,78,99,168,21,154,210,24,224,110,114,196,58,213,161,220,139,122,28,56,247,32,29,131,128,38,102,109,43,87,171,65,84,217,180,90,205,157,68,35,16,16,0,58,167,129,17,54,28,160,1,121,64,11,107,154,181,35,39,160,64,6,111,0,13,186,92,224,0,158,96,62,72,0,230,248,208,232,97,0,174,62,200,208,134,32,238,232,158,232,81,136,96,254,120,81,144,14,14,232,136,176,232,176,32,0,190,101,64,0,0/embed/fr-fr"
    
            return render_template('trajet.html',duree_trajet=duree_trajet,direction_trajet=direction_trajet)
        else :
            autonomie_manquante = int(distance) - int(autonomie)
            return render_template('notenough.html',autonomie_manquante=autonomie_manquante)

        # Generate just a boring response
        #return 'The cities are %s and %s ' % (ville_a, ville_b) 


    # Otherwise this was a normal GET request
    else:   
        return render_template('index.html')