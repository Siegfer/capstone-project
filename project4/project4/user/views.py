# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    """List members."""
    return render_template("users/members.html")



@blueprint.route("/search", methods=["GET"])
@login_required
def search():
    """search all plants within API"""
    req = requests.get(
        "https://api.boardgameatlas.com/api/search?limit=5&client_id=s2XQYtohOX"
    )
    data = json.loads(req.content)
    return render_template("users/search.html", data=data["games"])
