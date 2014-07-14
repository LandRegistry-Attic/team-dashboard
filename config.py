import os

class Config(object):
    DEBUG = False

class HerokuConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    TESTING = True
