from zeep import Client

def duree_trajet(distance,vit_moy) :
    client = Client('http://192.168.141.39:8000/?wsdl')
    result = client.service.addition(distance,vit_moy)
    return(result)