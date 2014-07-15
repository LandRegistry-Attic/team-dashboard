import os, logging
from flask import Flask
from flask.ext.basicauth import BasicAuth

app = Flask(__name__)

app.config.from_object(os.environ.get('SETTINGS'))

if os.environ.get('BASIC_AUTH_USERNAME'):
    app.config['BASIC_AUTH_USERNAME'] = os.environ['BASIC_AUTH_USERNAME']
    app.config['BASIC_AUTH_PASSWORD'] = os.environ['BASIC_AUTH_PASSWORD']
    app.config['BASIC_AUTH_FORCE'] = True
    basic_auth = BasicAuth(app)

print "============"
print app.config
print "============"

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

# jinja filter first name
def first_name(string):
    return string.strip().split()[0]

app.jinja_env.filters['first_name'] = first_name

