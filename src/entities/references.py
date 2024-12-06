class References:
    def __init__(
        self,
        id=None,
        reference_id=None,
        reference_type=None,
        created_at=None,
        author=None,
        title=None,
        year=None,
        booktitle=None,
        editor=None,
        volume=None,
        number=None,
        series=None,
        pages=None,
        address=None,
        month=None,
        organization=None,
        publisher=None,
        journal=None,
        note=None
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
    def to_dict(self):
        fields = vars(self)

        # Include all attributes
        return dict(fields.items())

    def __str__(self):
        return f"Title: {self.title}, author: {self.author}"
