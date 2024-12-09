import unittest
from validate import validate_book, validate_article, UserInputError
from db_helper import reset_db
from config import app
#pylint: disable = E1120
class TestValidation(unittest.TestCase):

    def setUp(self):
        # Push the app context to use the Flask app's resources
        self.app_context = app.app_context()
        self.app_context.push()
        reset_db()

    def test_validate_book_valid(self):
        try:
            validate_book("ref01", "Author Name", "2023", "Book Title", "Publisher", "City")
        except Exception:
            self.fail("validate_book raised an exception unexpectedly!")

    def test_validate_book_missing_field(self):
        with self.assertRaises(TypeError):  # Expect TypeError due to missing arguments
            validate_book("ref01", "Author Name", 2023, "Book Title")

    def test_validate_article_invalid_year(self):
        with self.assertRaises(UserInputError):
            validate_article("ref02", "Author Name", "Article Title",
                             "Journal Name", "abcd", 1, 2, "10-20", "Jan", None)
