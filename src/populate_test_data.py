from config import db
from test_data import test_data
from sqlalchemy import text
from validate import validate_article, validate_book, validate_inproceedings
from repositories.references_repository import create_reference

table_name = "reference"


def populate_database():
    for reference in test_data:
        create_reference(reference_id=reference["reference_id"],
                         reference_type=reference["reference_type"],
                         title=reference["title"],
                         author=reference["author"],
                         year=reference["year"],
                         booktitle=reference.get("booktitle"),
                         editor=reference.get("editor"),
                         volume=reference.get("volume"),
                         number=reference.get("number"),
                         series=reference.get("series"),
                         pages=reference.get("pages"),
                         address=reference.get("address"),
                         journal=reference.get("journal"),
                         month=reference.get("month"),
                         note=reference.get("note"),
                         organization=reference.get("organization"),
                         publisher=reference.get("publisher"),)
