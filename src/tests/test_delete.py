from app import get_references
from db_helper import reset_db
import unittest
from config import app

class TestDeleteReference(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()  # Flask test client
        self.app_context = app.app_context()
        self.app_context.push()
        reset_db()  # Reset the database before each test

    def tearDown(self):
        reset_db()  # Clean up database after each test
        self.app_context.pop()

    def test_create_and_delete_reference(self):
        # Submit a new reference via POST
        response = self.client.post(
            "/create_reference",
            data={
                "reference_type": "improceedings",
                "author": "John Doe",
                "title": "Sample imp",
                "booktitle": "Sample Title",
                "year": "2023",
                "publisher": "Sample Publisher"
            },
            follow_redirects=True,
        )
        # Checks if reference is added
        self.assertEqual(response.status_code, 200)
        references = get_references()
        self.assertEqual(len(references), 1)
        self.assertEqual(references[0].reference_id, "Sam2023")

        # Delete the reference
        reference_id = references[0].id  # Get the reference_id instead of 'id'
        response = self.client.post(f"/delete/{reference_id}", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check if the reference is deleted from the database
        references_1 = get_references()
        self.assertEqual(len(references_1), 0)
