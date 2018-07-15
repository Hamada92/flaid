import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wf9023j9'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')

config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}