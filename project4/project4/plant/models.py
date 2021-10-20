# -*- coding: utf-8 -*-
"""Plant models."""

from project4.database import Column, PkModel, db


class Plant(PkModel):
    """ model for plant """
    __tablename__ = "plants"
    AlternateName = Column(db.String(80), nullable=True, default=None)
    Edible = Column(db.String(80), nullable=True, default=None)
    EdibleParts = Column(db.String(80), nullable=True, default=None)
    EdibleUses = Column(db.String(80), nullable=True, default=None)
    Family = Column(db.String(80))
    Growth = Column(db.String(10), nullable=True, default=None)
    Height = Column(db.String(80))
    Habitat = Column(db.String(80), nullable=True, default=None)
    Layer = Column(db.String(80), nullable=True, default=None)
    Leaves = Column(db.String(80), nullable=True, default=None)
    LifeCycle = Column(db.String(80), nullable=True, default=None)
    LightRequirement = Column(db.String(80))
    Name = Column(db.String(80))
    GermanName=Column(db.String(80), nullable=True, default=None)
    PlantsForAFuture = Column(db.String(80))
    ScientificName = Column(db.String(80), unique=True)
    SoilType = Column(db.String(80))
    UsdaHardinessZone = Column(db.String(80))
    Utility = Column(db.String(80), nullable=True, default=None)
    WaterRequirement = Column(db.String(80))
    Wikipedia = Column(db.String(80))
    _Warning = Column(db.String(80), nullable=True, default=None)

    @property
    def name(self):
        """Scientific name."""
        return f"{self.ScientificName}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Plant({self.Name!r})>"
