from flask import render_template, send_file

from team import app
from members import Members
from whereabouts import Whereabouts

members = Members().load("../team-data/data/team.tsv")
whereabouts = Whereabouts().load("../team-data/data/whereabouts.tsv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cards')
def _cards():
    return render_template('cards.html', members=members.members)

@app.route('/whereabouts')
def _whereabouts():
    places = whereabouts.places('2014-07-11')
    return render_template('whereabouts.html', members=members.members, places=places)

@app.route('/photos/<path>')
def _photo(path):
    return send_file("../../team-data/data/photos/" + path, mimetype='image/jpeg')

