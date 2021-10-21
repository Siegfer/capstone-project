import json

from . import db
from models import Plant

def seed(filename):
    s = db.session()
    with open(filename, "wb") as f:
        data = json.load(f)
        plants = [Plant(**p) for p in data]
        s.bulk_save_objects(plants)



