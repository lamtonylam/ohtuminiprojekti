import datetime
from repositories.references_repository import get_reference_id
from entities.references import References


class UserInputError(Exception):
    pass


def should_be_str(param_name, value):
    if not isinstance(value, str) or len(value) < 1:
        raise UserInputError(f"{param_name} is too short or invalid.")


def should_be_valid_positive_int(param_name, value):
    if value:
        try:
            number = int(value)
        except ValueError as exc:
            raise UserInputError(f"{param_name} must be a positive integer.") from exc
        if number <= 0:
            raise UserInputError(f"{param_name} must be a positive integer.")

def year_check(year):
    should_be_valid_positive_int("year", year)
    if int(year) > datetime.date.today().year:
        raise UserInputError(
            "year must be a valid integer between 1 and current year.")


def reference_id_should_be_unique(value):
    references = get_reference_id()
    if value in references:
        raise UserInputError(
            "reference ID already exists in the database."
        )


def month_check(month):
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]
    if month:
        should_be_str("month", month)
    if month and (month.lower() not in months):
        raise UserInputError(f"month must be one of: {', '.join(months)}.")

def validate_article(reference: References):
    should_be_str("journal", reference.journal)
    should_be_valid_positive_int("volume", reference.volume)

    for field_name in ["number", "pages", "note"]:
        value = getattr(reference, field_name)
        if value:
            should_be_str(field_name, value)

    if reference.month:
        month_check(reference.month)

def validate_book(reference: References):
    should_be_str("publisher", reference.publisher)
    should_be_str("address", reference.address)

def validate_inproceedings(reference: References):
    should_be_str("booktitle", reference.booktitle)
    should_be_valid_positive_int("volume", reference.volume)

    for field_name in [
        "editor",
        "volume",
        "number",
        "series",
        "pages",
        "address",
        "organization",
        "publisher",
    ]:
        value = getattr(reference, field_name)
        if value:
            should_be_str(field_name, value)

    if reference.month:
        month_check(reference.month)


def validate_reference(reference: References):
    reference_id_should_be_unique(reference.reference_id)
    should_be_str("reference_id", reference.reference_id)
    should_be_str("author", reference.author)
    should_be_str("title", reference.title)
    year_check(reference.year)

    # conditional validations based on reference type
    if reference.reference_type == "article":
        validate_article(reference)
    elif reference.reference_type == "book":
        validate_book(reference)
    elif reference.reference_type == "inproceedings":
        validate_inproceedings(reference)
    else:
        raise UserInputError(f"Unsupported reference type: {reference.reference_type}")
