import unittest
from validate import (
    validate_inproceedings,
    UserInputError,
    validate_article,
)
from config import app


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        self.valid_inproceedings = {
            "reference_id": "ref001",
            "author": "John Doe",
            "title": "An Innovative Approach to AI",
            "booktitle": "Proceedings of the AI Conference",
            "year": "2024",
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

        self.valid_article = {
            "reference_id": "ref002",
            "author": "Smith, John and Doe, Jane",
            "title": "An Example Article for BibTeX",
            "journal": "Journal of Examples",
            "year": "2023",
            "volume": "15",
            "number": "4",
            "pages": "123-134",
            "month": None,
            "note": None,
        }

        self.valid_book = {
            "reference_id": "ref003",
            "author": "Johnson, Emily and Brown, Michael",
            "year": "2023",
            "title": "An Example Book for BibTeX",
            "publisher": "Example Publisher",
            "address": "New York",
        }

    def test_input_not_string(self):
        self.valid_inproceedings["reference_id"] = 123
        with self.assertRaises(UserInputError):
            validate_inproceedings(*self.valid_inproceedings)

    def test_input_negative_int(self):
        self.valid_inproceedings["volume"] = "-5"
        with self.assertRaises(UserInputError):
            validate_inproceedings(*self.valid_inproceedings)

    def test_input_negative_year(self):
        self.valid_inproceedings["year"] = "3020"
        with self.assertRaises(UserInputError):
            validate_inproceedings(*self.valid_inproceedings)

    def test_invalid_month(self):
        self.valid_inproceedings["month"] = "Octember"
        with self.assertRaises(UserInputError):
            validate_inproceedings(*self.valid_inproceedings)

    def test_required_field_missing(self):
        del self.valid_inproceedings["title"]
        with self.assertRaises(TypeError):
            validate_inproceedings(*self.valid_inproceedings)

    def test_valid_input(self):
        try:
            validate_inproceedings(**self.valid_inproceedings)
        except UserInputError:
            self.fail(
                "validate_inproceedings raised UserInputError unexpectedly!")

    def test_article_input_not_string(self):
        self.valid_article["author"] = 222
        with self.assertRaises(UserInputError):
            validate_article(*self.valid_article)

    def test_article_input_negative_int(self):
        self.valid_article["volume"] = -23
        with self.assertRaises(UserInputError):
            validate_article(*self.valid_article)

    def test_article_input_negative_year(self):
        self.valid_article["year"] = -11
        with self.assertRaises(UserInputError):
            validate_article(*self.valid_article)

    def test_article_invalid_month(self):
        self.valid_article["month"] = "joulukuu"
        with self.assertRaises(UserInputError):
            validate_article(*self.valid_article)

    def tearDown(self):
        self.app_context.pop()
