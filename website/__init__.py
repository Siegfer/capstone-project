import json
import click
from os import path
from flask import Flask
from flask.cli import with_appcontext
from flask_login import LoginManager
from flask_seeder import FlaskSeeder
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "capstone-project.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "not-so-secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    create_database(app)
    
    seeder = FlaskSeeder()
    seeder.init_app(app, db)
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

@click.command()
@click.option('--filename', default="seed.json", help='Filename for the json file to be used for seeding the db')
def add_plants(filename):
    """
    Migrate plants in seed file to database
    """
    click.echo('Adding plants to db...')
    from .models import Plant

    count = 0
    with open(filename) as f:
        data = json.load(f)
        plants = [Plant(**p) for p in data.values()]
        count = len(plants)
        db.session.add_all(plants)
        db.session.commit()
    return click.echo(f'{count} plants were added successfully to the database.')




def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
