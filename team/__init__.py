import os, logging
from flask import Flask

app = Flask(__name__)

app.config.from_object(os.environ.get('SETTINGS'))

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

