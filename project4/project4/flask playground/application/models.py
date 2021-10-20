from . import db


class Plant(db.Model):
    """Data model for user accounts."""
    __tablename__ = 'plants'
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
    GermanName=db.Column(db.String(80), nullable=True, default=None)
    PlantsForAFuture = db.Column(db.String(80))
    ScientificName = db.Column(db.String(80), unique=True, foreign_key=True)
    SoilType = db.Column(db.String(80))
    UsdaHardinessZone = db.Column(db.String(80))
    Utility = db.Column(db.String(80), nullable=True, default=None)
    WaterRequirement = db.Column(db.String(80))
    Wikipedia = db.Column(db.String(80))
    
def __repr__(self):
    return '<Plant{}>'.format(self.ScientificName)