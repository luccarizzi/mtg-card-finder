from flask import Blueprint, render_template, request
import requests
import json

views = Blueprint(__name__, 'views')

url = 'https://api.scryfall.com/cards/named?exact='

data = {}

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        card_name = request.form['card_name'].replace(' ', '+')
        try:
            response = json.loads(requests.request('GET', f'{url}{card_name}').text)
            data['name'] = response['name']
            data['image'] = response['image_uris']['normal']
            return render_template('image.html', image_uri=data['image'])
        except Exception as e:
            return render_template('not_found.html', card_name=request.form['card_name'])
    else:
        return render_template('index.html')
