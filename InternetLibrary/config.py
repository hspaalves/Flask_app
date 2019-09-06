import os


class Development(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://0.0.0.0:5432/Borges'


class Production(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://0.0.0.0:5432/Borges'


app_config = {
    'development': Development,
    'production': Production,
}
