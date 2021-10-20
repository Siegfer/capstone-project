from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
    """setting up core app"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    
    with app.app.context():
        from . import routes  # import routes
        db.create_all() # create SQL tables for our data models
        
        return app