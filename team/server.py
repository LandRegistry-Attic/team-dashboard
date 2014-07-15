from flask import render_template, send_file

from functools import wraps
from flask import request, Response
import time
import os
from team import app
from members import Members
from whereabouts import Whereabouts

team = Members().load(os.environ.get('TEAM_TSV_URL'))
whereabouts = Whereabouts().load(os.environ.get('WHEREABOUTS_TSV_URL'))

def check_auth(username, password):
    return username == os.environ.get('USERNAME') and password == os.environ.get('PASSWORD')

def authenticate():
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cards')
@requires_auth
def _cards():
    return render_template('cards.html', members=team.members)

@app.route('/whereabouts')
@requires_auth
def _whereabouts_today():
    today = time.strftime("%Y-%m-%d")
    return _whereabouts(today)

@app.route('/whereabouts/<date>')
@requires_auth
def _whereabouts(date):
    places = whereabouts.places(date)
    return render_template('whereabouts.html', date=date, members=team.members, places=places)


