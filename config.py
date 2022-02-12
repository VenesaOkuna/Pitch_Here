import os


class Config:
    
    '''
    General configuration parent class
    '''

    DB_USER = os.environ.get('DB_USER') or  ""
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or ""
    DB = 'pitchhere'
    
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost/{DB}'

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # SUBJECT_PREFIX = 'Watchlist'
    # SENDER_EMAIL = 'venesa.okuna@student.moringaschool.com'  


    # simple mde  configurations
    # SIMPLEMDE_JS_IIFE = True
    # SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venesa:1234@localhost/watchlist_test'



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venesa:1234@localhost/pitchhere'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}