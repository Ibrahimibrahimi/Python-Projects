from flask import Flask 
from logging.handlers import RotatingFileHandler
import logging
import os
from .routes import auth
from .routes import main
from .extensions  import login_manager , db
from .models import User

def create_app():
    # create flask
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(16) # for session
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
    # add routes
    app.register_blueprint(main.main_bp)
    app.register_blueprint(auth.auth_bp)
    
    # add database & create tables
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    # create admin account
    
    # configure login manager
    login_manager.init_app(app)
    
    # configure logger
    log_file = RotatingFileHandler(
        "./app/logs/main.log",
        maxBytes=10240,
        backupCount=5
    )
    log_file.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    app.logger.addHandler(log_file)
    app.logger.setLevel(logging.INFO)
    return app