# ElectroAppCalculator project 🚗

This is a project for course ETRS013 in master 2 at USMB.
The goal of this project is to create a web based app that will communicate with differents api.
There is a SOAP service, GraphQL api call and a flask app that will communicate with all apps.

## How to use this app ?
The API juste do somes math, this is for education purpose

### Without docker
1. Clone this repo `git clone https://github.com/Dede1441/electric_roadapp_etrs013.git`
2. Create venv `python -m venv .venv`
3. Activate venv `.venv\Script\Activate`
4. Install requirements `pip install -r requirements.txt`
5. Launch API : `/bin/python3 electric_roadapp_etrs013/electric_roadapp_api.p`
4. Run the APP : `flask --app electric_roadapp_interface run --host=0.0.0.0`



### With docker 🐋
1. Build API app in api  : `docker build . --tag electroapp_api`
2. Build APP : `docker build . --tag electroapp`
3. Run containers : `docker run -p 8000:8000 -d electroapp_api:latest` && `docker run -p 5000:5000 -d electroapp:latest`



### Question ?
If you want to contribute to this project/improve code open an issue


### Others projects 
[Nicolas Boulard Git](https://github.com/NicolasBoulard/carlee-frontend/)
