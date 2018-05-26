import os

class Config(object):
    SECRET_KEY = os.getenv('APP_SECRET')
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    THREADS_PER_PAGE = 2

class ProductionConfig(Config):
    ENV = 'prod'
    DEBUG = False

class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True

class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    TESTING = True