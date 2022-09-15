from flask import Flask, render_template, request
import electric_roadapp_client

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

            return render_template('time.html',duree_trajet=duree_trajet)
        else :
            autonomie_manquante = int(distance) - int(autonomie)
            return render_template('notenough.html',autonomie_manquante=autonomie_manquante)

        # Generate just a boring response
        #return 'The cities are %s and %s ' % (ville_a, ville_b) 


    # Otherwise this was a normal GET request
    else:   
        return render_template('index.html')