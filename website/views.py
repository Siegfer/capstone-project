import json
from . import db
from .models import Note, Plant
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, jsonify

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note is too short", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)


@views.route("/plants", methods=["GET"])
@login_required
def all_plants():
    # Do the search for user plants here. Include this once association is made
    # Ex:   db.session.query('FROM plant JOIN user SELECT * WHERE plant.user_id == user.id')
    results = db.session.query(Plant)
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
        plant_list.append(plant)

    return render_template("plant.html", user=current_user, plant_list=plant_list)


@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
