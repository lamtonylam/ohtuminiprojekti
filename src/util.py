class UserInputError(Exception):
    pass


def validate_inproceeding(
    reference_id,
    author,
    title,
    booktitle,
    year,
    editor=None,
    volume=None,
    number=None,
    series=None,
    pages=None,
    address=None,
    month=None,
    organization=None,
    publisher=None,
):

    # List of valid months
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

    # Validate required fields
    if not reference_id or not isinstance(reference_id, str) or len(reference_id) < 1:
        raise UserInputError("reference_id is too short or invalid.")
    if not author or not isinstance(author, str) or len(author) < 1:
        raise UserInputError("author is too short or invalid.")
    if not title or not isinstance(title, str) or len(title) < 1:
        raise UserInputError("title is too short or invalid.")
    if not booktitle or not isinstance(booktitle, str) or len(booktitle) < 1:
        raise UserInputError("booktitle is too short or invalid.")
    if int(year) <= 0 or int(year) > 2025:
        raise UserInputError("year must be a valid integer between 1 and 2025.")

    # Validate optional fields
    if month and (not isinstance(month, str) or month.lower() not in months):
        raise UserInputError(f"month must be one of: {', '.join(months)}.")

    if volume and int(volume) < 0:
        raise UserInputError("volume must be a positive integer.")
    if volume and volume.isalpha():
        raise UserInputError("volume must be a number")

    if number and int(number) < 0:
        raise UserInputError("number must be a positive integer.")
    if number and number.isalpha():
        raise UserInputError("number must be a number")

    for field_name, value in [
        ("editor", editor),
        ("series", series),
        ("pages", pages),
        ("address", address),
        ("organization", organization),
        ("publisher", publisher),
    ]:
        if value and (not isinstance(value, str) or len(value) < 1):
            raise UserInputError(
                f"{field_name} must be a non-empty string if provided."
            )
