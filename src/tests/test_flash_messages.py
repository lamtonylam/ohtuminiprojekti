from config import app
from db_helper import reset_db
import unittest


class TestFlashMessages(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        # Create a test client
        self.client = app.test_client()
        reset_db()

    def test_reference_creation_flash_success(self):
        response = self.client.post(
            "/create_reference",
            data={
                "reference_id": "ref01",
                "author": "Author Name",
                "title": "Book Title",
                "year": "2023",
                "reference_type": "book",
                "publisher": "Publisher",
                "address": "City",
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect
