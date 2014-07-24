import os

class Config(object):
    DEBUG = False
    BASIC_AUTH_USERNAME = ''
    BASIC_AUTH_PASSWORD = ''
    TEAM_TSV_URL = 'data/team.tsv'
    WHEREABOUTS_TSV_URL = 'data/whereabouts.tsv'
    PHOTO_URL = ''
    PHOTO_USERNAME = ''
    PHOTO_PASSWORD = ''

class ProductionConfig(Config):
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
    TEAM_TSV_URL = os.environ.get('TEAM_TSV_URL')
    WHEREABOUTS_TSV_URL = os.environ.get('WHEREABOUTS_TSV_URL')
    PHOTO_URL = os.environ.get('PHOTO_URL')
    PHOTO_USERNAME = os.environ.get('PHOTO_USERNAME')
    PHOTO_PASSWORD = os.getenv('PHOTO_PASSWORD', '')

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    TESTING = True
