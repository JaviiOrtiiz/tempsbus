import requests
import json
from datetime import datetime
# Flask
from flask import Flask, request, jsonify


url = "https://api.tmb.cat/v1/itransit/bus/parades/2234?agrupar_desti=true&app_id=4c132798&app_key=8504ae3a636b155724a1c7e140ee039f&numberOfPredictions=2"

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

def get_time():
    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)

    for i in range(len(data['parades'][0]['linies_trajectes'])):
        if data['parades'][0]['linies_trajectes'][i]['nom_linia'] == 'V23':
            arrival_time = datetime.fromtimestamp(int(data['parades'][0]['linies_trajectes'][i]['propers_busos'][0]['temps_arribada']/1000))

    current_time = datetime.now()

    mins = (arrival_time - current_time).total_seconds()/60

    return('Quedan {} minutos'.format(round(mins)))

app = Flask(__name__)

# no html, just a string
@app.route('/', methods=['GET'])
def home():
    return get_time()