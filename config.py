import os

class Config(object):
    DEBUG = False
    TEAM_TSV_URL = os.getenv("TEAM_TSV_URL", "team/data/team.tsv")
    WHEREABOUTS_TSV_URL = os.getenv("WHEREABOUTS_TSV_URL", "team/data/whereabouts.tsv")

class HerokuConfig(Config):
    DEBUG = False
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    TESTING = True
