import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wf9023j9'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    Debug = True

config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}