import unittest
from config import app
from db_helper import reset_db
from repositories.references_repository import get_references, create_reference

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()  # Flask test client
        self.app_context = app.app_context()
        self.app_context.push()
        reset_db()  # Reset the database before each test

    def tearDown(self):
        reset_db()  # Clean up database after each test
        self.app_context.pop()

    def test_index_route(self):
        # Test the index route
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"References", response.data)

    def test_preview_route(self):
        # Add a reference to the database
        create_reference(
            reference_id="ref01",
            reference_type="article",
            title="Test Article",
            author="Jane Doe",
            year="2023",
            journal="Test Journal",
            volume="1",
            number="1",
            pages="1-10",
            month=None,
            note=None,
        )

        # Test the preview route
        response = self.client.get("/preview")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"@article", response.data)

    def test_new_reference_route(self):
        # Test the new reference form
        response = self.client.get("/new_reference")
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b"Add a New Reference", response.data)

    def test_create_reference(self):
        # Submit a new reference via POST
        response = self.client.post(
            "/create_reference",
            data={
                "reference_id": "ref02",
                "reference_type": "improceedings",
                "author": "John Doe",
                "title": "Sample imp",
                "booktitle": "Sample Title",
                "year": "2023",
                "publisher": "Sample Publisher"
            },
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b"Added successfully", response.data)

        # Verify the reference was added
        references = get_references()
        print(references)
        self.assertEqual(len(references), 1)
        self.assertEqual(references[0].reference_id, "ref02")

    def test_download_route(self):
        # Add a reference
        create_reference(
            reference_id="ref03",
            reference_type="book",
            title="Test Book",
            author="Alice",
            year="2022",
            publisher="Test Publisher",
        )

        # Test the download route
        response = self.client.get("/download")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"@book", response.data)
        self.assertIn(b"Test Book", response.data)

    def test_reset_db_route(self):
        # Add a reference
        create_reference(
            reference_id="ref04",
            reference_type="article",
            title="Temporary Article",
            author="Bob",
            year="2021",
            journal="Test Journal",
        )

        # Reset the database using the test route
        response = self.client.get("/reset_db")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"db reset", response.data)

        # Verify the database is empty
        references = get_references()
        self.assertEqual(len(references), 0)


if __name__ == "__main__":
    unittest.main()
