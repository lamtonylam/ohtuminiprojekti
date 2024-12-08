from repositories.references_repository import get_references, create_reference
from db_helper import reset_db
import unittest

from config import app

class TestDatabaseOperations(unittest.TestCase):
    
    def setUp(self):
        # Push the app context to use the Flask app's resources
        self.app_context = app.app_context()
        self.app_context.push()
        reset_db()  # Ensure a clean slate

    def test_create_and_get_references(self):
        # Sample reference data
        reference = {
            "reference_id": "ref001",
            "reference_type": "inproceedings",
            "author": "John Doe",
            "title": "An Innovative Approach to AI",
            "booktitle": "Proceedings of the AI Conference",
            "year": 2024,
            "editor": "Jane Smith",
            "volume": "1",
            "number": "1",
            "series": "AI Series",
            "pages": "1-10",
            "address": "New York, NY",
            "month": "November",
            "organization": "AI Society",
            "publisher": "Tech Press",
        }

        create_reference(**reference)  # Assuming this function adds a reference
        references = get_references()  # Get references after adding

        # Check if the reference was added correctly
        self.assertGreater(len(references), 0)  # Ensure there is at least one reference

        # If 'references' is a list of objects, you should access its attributes, not index directly
        # Assuming references is a list of objects, you can check one object like this
        first_reference = references[0]  # This assumes references is a list
        self.assertEqual(first_reference.reference_id, "ref001")
        self.assertEqual(first_reference.author, "John Doe")
        self.assertEqual(first_reference.title, "An Innovative Approach to AI")
        self.assertEqual(first_reference.year, 2024)

    def test_reset_db(self):
        # Test resetting the database
        reset_db()  # Assuming reset_db resets the database

        # Verify the database state after reset
        references = get_references()
        self.assertEqual(len(references), 0)  # Assuming the database is empty after reset

    def tearDown(self):
        # Pop the app context to clean up after the test
        self.app_context.pop()