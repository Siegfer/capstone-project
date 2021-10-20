from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Plant

@app.route('/', methods=['GET'])
def plant_records():
    """Create a plant by query string parameters"""
    Name = request.args.get('Name')
    ScientificName = request.args.get('ScientificName')
    if Name and ScientificName:
        new_plant = Plant(
        Family = "Caprifoliaceae",
        Growth = "Medium",
        Height = "3.5",
        Layer = "Shrubs",
        LightRequirement = "Full sun, Partial sun/shade",
        Name = "Indian Abelia",
        PlantsForAFuture = "Https://pfaf.org/user/plant.aspx?latinname=abelia triflora",
        ScientificName = "Abelia triflora",
        SoilType = "Light (sandy), Medium",
        UsdaHardinessZone = "5-9",
        WaterRequirement = "Dry, Moist"
        )
        db.session.add(new_plant) # add new Plant
        db.session.commit()
    return make_response(f"{new_plant} successfully created!" )
    