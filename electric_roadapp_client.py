from zeep import Client

def duree_trajet(distance,vit_moy) :
    client = Client('https://morning-temple-96784.herokuapp.com/?wsdl')
    result = client.service.calcul_heures(distance,vit_moy)
    return(result)