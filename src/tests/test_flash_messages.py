from app import reference_creation
from flask import Flask, request
import unittest

class TestFlashMessages(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.secret_key = "test_key"
        self.client = self.app.test_client()

    def test_reference_creation_flash_success(self):
        with self.app.test_request_context(
            '/create_reference', 
            method='POST',
            data={
                "reference_id": "ref01",
                "author": "Author Name",
                "title": "Book Title",
                "year": "2023",
                "reference_type": "book",
                "publisher": "Publisher",
                "address": "City",
            }
        ):
            response = reference_creation()
            self.assertEqual(response.status_code, 302)  # Redirect
