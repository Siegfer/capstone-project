from . import db
from .models import Plant
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for

plant = Blueprint("plant", __name__)

@plant.route("/plant-list")
def create_list():
    pass

@plant.route('/plant/search', methods=['POST'])
def search_plant():
    plant_id = request.form.get("id")
    plant_name = request.form.get("plant")
    if plant_id != "": 
        results = db.session.query(Plant).filter(Plant.id == plant_id)
    elif plant_name != "":
        results = db.session.query(Plant).filter(Plant.ScientificName == plant_name)
    plant_list = []
    for result in results:
        plant = {
            "id": result.id, 
            "Name": result.Name,
            "Growth": result.Growth,
            "ScientificName": result.ScientificName,
            "LightRequirement": result.LightRequirement,
            "SoilType": result.SoilType,
            "WaterRequirement": result.WaterRequirement,
            "Wikipedia": result.Wikipedia,
            "Edible": result.Edible,
            "EdibleParts": result.EdibleParts,
            "Family": result.Family,
            "LifeCycle": result.LifeCycle,
            }
    pass