class UserInputError(Exception):
    pass


def validate_inproceeding(reference_id, author, title, booktitle, year):
    if (
        len(reference_id) < 1
        or len(author) < 1
        or len(title) < 1
        or len(booktitle) < 1
        or not year
    ):
        raise UserInputError("Please fill the mandatory fields")
