from flask import render_template, send_file

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
def _whereabouts():
    places = whereabouts.places('2014-07-11')
    return render_template('whereabouts.html', members=team.members, places=places)

@app.route('/photos/<path>')
def _photo(path):
    return send_file("../../team-data/photos/" + path, mimetype='image/jpeg')

