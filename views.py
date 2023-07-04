from flask import Blueprint, render_template, request, redirect, url_for
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
            return redirect(url_for('views.output'))
        except Exception as e:
            return redirect(url_for('views.not_found'))
    else:
        return render_template('index.html')

@views.route('/output')
def output():
    return data

@views.route('/not_found')
def not_found():
    return 'PAGE NOT FOUND'