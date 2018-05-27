import os

class Config(object):
    SECRET_KEY = os.getenv('APP_SECRET')
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    THREADS_PER_PAGE = 2
    MODELS_DIR = os.path.join(BASE_DIR, 'models')

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