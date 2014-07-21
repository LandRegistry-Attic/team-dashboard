import time

from flask import render_template
from flask import Response

from team import app
from members import Members
from whereabouts import Whereabouts
from photos import Photos


team = Members().load(app.config['TEAM_TSV_URL'])

whereabouts = Whereabouts().load(app.config['WHEREABOUTS_TSV_URL'])

photos = Photos(app.config['PHOTO_URL'],
    username=app.config.get('PHOTO_USERNAME', ''),
    password=app.config.get('PHOTO_PASSWORD', ''))


@app.route('/')
def _home():
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

@app.route('/photo/<photo>')
def _photo(photo):
    content, content_type = photos.get(photo)
    return Response(content, content_type=content_type)
