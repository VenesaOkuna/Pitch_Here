import os
from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig, config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager




login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


db = SQLAlchemy()
bootstrap = Bootstrap()

# photos = UploadSet('photos',IMAGES)
# mail = Mail()

def create_app(config_name):

    app = Flask(__name__)  
      
    # Creating the app configurations

    app.config.from_object(config_options['development'])
    config_options['development'].init_app(app)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # mail.init_app(app)



    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    # setting config
    from .requests import configure_request
    configure_request(app)



    # configure UploadSet
    # configure_uploads(app,photos)


    return app