from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import json

db = SQLAlchemy()
DB_NAME = "capstone-project.db"
SEED_FILEPATH="/Users/siegfer/Documents/Class/Unit-4/Capstone Project/capstone-project/website/test_scrape_dump.json"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "not-so-secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note, Plant

    create_database(app)
    
    def seed(filename):
        # s = db.session()
        with open(filename) as f:
            data = json.load(f)
            plants = [Plant(**p) for p in data.values()]
            db.session.add_all(plants)
            db.session.commit()
    seed(SEED_FILEPATH)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
