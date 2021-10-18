import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from leaf_it_to_me.extensions import db
    from leaf_it_to_me.models import User

    click.echo("create user")
    user = User(username="siegfer", email="nicholasquoctran@gmail.com", password="nicky1988", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
