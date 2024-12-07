from test_data import test_data
from repositories.references_repository import create_reference
from entities.references import References

table_name = "reference"


def populate_database():
    for reference in test_data:
        create_reference(References(**reference))
