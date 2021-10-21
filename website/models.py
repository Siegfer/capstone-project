from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    AlternateName = db.Column(db.String(80), nullable=True, default=None)
    Edible = db.Column(db.String(80), nullable=True, default=None)
    EdibleParts = db.Column(db.String(80), nullable=True, default=None)
    EdibleUses = db.Column(db.String(80), nullable=True, default=None)
    Family = db.Column(db.String(80))
    Growth = db.Column(db.String(10), nullable=True, default=None)
    Height = db.Column(db.String(80))
    Habitat = db.Column(db.String(80), nullable=True, default=None)
    Layer = db.Column(db.String(80), nullable=True, default=None)
    Leaves = db.Column(db.String(80), nullable=True, default=None)
    LifeCycle = db.Column(db.String(80), nullable=True, default=None)
    LightRequirement = db.Column(db.String(80))
    Name = db.Column(db.String(80))
    GermanName = db.Column(db.String(80), nullable=True, default=None)
    PlantsForAFuture = db.Column(db.String(80))
    ScientificName = db.Column(db.String(80), unique=True)
    SoilType = db.Column(db.String(80))
    UsdaHardinessZone = db.Column(db.String(80))
    Utility = db.Column(db.String(80), nullable=True, default=None)
    WaterRequirement = db.Column(db.String(80))
    Wikipedia = db.Column(db.String(80))
    Warning = db.Column(db.String(80), nullable=True, default=None)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship("Note")
    plants = db.relationship("Plant")
