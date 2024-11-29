class Inproceedings:
    def __init__(
        self,
        id,
        reference_id,
        reference_type,
        created_at,
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
        journal,
        note
    ):
        self.id = id
        self.reference_id = reference_id
        self.reference_type = reference_type
        self.created_at = created_at
        self.author = author
        self.title = title
        self.booktitle = booktitle
        self.year = year
        self.editor = editor
        self.volume = volume
        self.number = number
        self.series = series
        self.pages = pages
        self.address = address
        self.month = month
        self.organization = organization
        self.publisher = publisher
        self.journal = journal
        self.note = note

    # returns a dictionary of the class types
    # left out self.id, self.created_at as they are not relevant in bibtex generation
    def to_dict(self):
        fields = {
            "reference_type": self.reference_type,
            "author": self.author,
            "year": self.year,
            "title": self.title,
            "booktitle": self.booktitle,
            "editor": self.editor,
            "volume": self.volume,
            "number": self.number,
            "series": self.series,
            "pages": self.pages,
            "address": self.address,
            "month": self.month,
            "organization": self.organization,
            "publisher": self.publisher,
            "journal": self.journal,
            "note": self.note
        }

        result = {}
        for key, value in fields.items():
            if value is not None:
                result[key] = value

        return result

    def __str__(self):
        return f"Title: {self.title}, author: {self.author}"
