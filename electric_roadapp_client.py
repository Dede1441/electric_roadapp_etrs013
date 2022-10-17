from zeep import Client

def duree_trajet(distance,vit_moy) :
    client = Client('http://172.18.2.1:8000/?wsdl')
    result = client.service.calcul_heures(distance,vit_moy)
    return(result)