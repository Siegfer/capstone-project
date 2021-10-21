import json

from . import db
from .models import Plant


def seed(filename: str) -> None:
    s = db.session()
    with open(filename, "wb") as f:
        data = json.load(f)
        plants = [Plant(**p) for p in data]
        s.bulk_save_objects(plants)


if __name__ == "__main__":
    seed("test_scrape_dump.json")
