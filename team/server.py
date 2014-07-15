from flask import render_template, send_file

import time
from team import app
from members import Members
from whereabouts import Whereabouts

team = Members().load("../team-data/team.tsv")
whereabouts = Whereabouts().load("../team-data/whereabouts.tsv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cards')
def _cards():
    return render_template('cards.html', members=team.members)

@app.route('/whereabouts')
def _whereabouts_today():
    today = time.strftime("%Y-%m-%d")
    return _whereabouts(today)

@app.route('/whereabouts/<date>')
def _whereabouts(date):
    places = whereabouts.places(date)
    return render_template('whereabouts.html', date=date, members=team.members, places=places)

@app.route('/photos/<path>')
def _photo(path):
    return send_file("../../team-data/photos/" + path, mimetype='image/jpeg')

