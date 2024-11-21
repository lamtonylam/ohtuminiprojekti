import datetime

class UserInputError(Exception):
    pass

def validate_inproceeding(
    reference_id,
    author,
    title,
    booktitle,
    year,
    editor,
    volume,
    number,
    series,
    pages,
    address,
    month,
    organization,
    publisher,
):
    def should_be_str(param_name, value):
        if not value or not isinstance(value, str) or len(value) < 1:
            raise UserInputError(f"{param_name} is too short or invalid.")

    def should_be_valid_positive_int(param_name, value):
        if value and not value.isnumeric():
            raise UserInputError(f"{param_name} must be a positive integer.")

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
    should_be_str("reference_id", reference_id)
    should_be_str("author", author)
    should_be_str("title", title)
    should_be_str("booktitle", booktitle)

    should_be_valid_positive_int("year", year)
    if int(year) > datetime.date.today().year:
        raise UserInputError("year must be a valid integer between 1 and current year.")

    # Validate optional fields
    if month:
        should_be_str("month", month)
    if month and (month.lower() not in months):
        raise UserInputError(f"month must be one of: {', '.join(months)}.")
    
    should_be_valid_positive_int("volume", volume)
    should_be_valid_positive_int("number", number)

    for field_name, value in [
        ("editor", editor),
        ("series", series),
        ("pages", pages),
        ("address", address),
        ("organization", organization),
        ("publisher", publisher),
    ]:
        if value:
            should_be_str(field_name, value)
