import os

class Config(object):
    DEBUG = False

class HerokuConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    TEAM_TSV_URL = "team/data/team.tsv"
    WHEREABOUTS_TSV_URL = "team/data/whereabouts.tsv"
    PHOTOS_DIR = "team/data/photos"

class TestConfig(Config):
    DEBUG = True
    TESTING = True
