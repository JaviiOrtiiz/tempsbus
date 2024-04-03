import requests
import json
from datetime import datetime
import os
# Flask
from flask import Flask, request, jsonify
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

# URL to get the bus arrival time
url = "https://api.tmb.cat/v1/itransit/bus/parades/2234?agrupar_desti=true&app_id=4c132798&app_key=8504ae3a636b155724a1c7e140ee039f&numberOfPredictions=2"

# Headers and payload
payload = {}
headers = {
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'es-ES,es;q=0.9',
  'cache-control': 'no-cache',
  'origin': 'https://www.tmb.cat',
  'pragma': 'no-cache',
  'referer': 'https://www.tmb.cat/',
  'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

# Function to get the bus arrival time
def get_time():
    '''Get the bus arrival time and return a message with the time left for the bus to arrive'''
    # Perform the request
    response = requests.request("GET", url, headers=headers, data=payload)

    # Parse the response
    data = json.loads(response.text)

    # Get the arrival time from the response
    for i in range(len(data['parades'][0]['linies_trajectes'])):
        if data['parades'][0]['linies_trajectes'][i]['nom_linia'] == 'V23':
            arrival_time = datetime.fromtimestamp(int(data['parades'][0]['linies_trajectes'][i]['propers_busos'][0]['temps_arribada']/1000))

    # Calculate the time left for the bus to arrive
    mins = round((arrival_time - datetime.now()).total_seconds()/60)

    # Generate the message
    if mins == 0:
        msg = '¡Queda menos de un minuto! Corre, mi chocolatito!'
    elif mins == 1:
        msg = '¡Queda un minuto! Corre, mi chocolatito!'
    elif mins < 5:
        msg = 'Dale gas, que quedan {} minutos'.format(mins)
    elif mins > 10:
        msg = 'Relax bombona, que te quedan {} minutos'.format(mins)
    else:
        msg = 'Quedan {} minutos'.format(mins)
    
    # Log the info about the request (deactivated for now)
    logging.info('Tiempo de bus solicitado, con llegada en {} minutos'.format(mins))
    
    # Return the message
    return msg


app = Flask(__name__)

# no html, just a string
@app.route('/', methods=['GET'])
def home():
    return get_time()