from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from repositories.references_repository import get_references, create_reference
from config import app, test_env, populate_env
from validate import validate_reference
from populate_test_data import populate_database
from bibtex_parser import reference_bibtex_parser
from entities.references import References


@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)


# get a preview of the bibtex
@app.route("/preview")
def bibtexpreview():
    references = get_references()
    return render_template(
        "preview.html",
        reference_list_bibtex=reference_bibtex_parser(references),
    )


@app.route("/new_reference")
def new():
    return render_template("new_reference.html")


@app.route("/create_reference", methods=["POST"])
def reference_creation():
    mandatory_fields = ["reference_id", "author", "title", "year", "reference_type"]
    optional_fields = [
        "booktitle", "editor", "volume", "number", "series", "journal", "note",
        "pages", "address", "month", "organization", "publisher"
    ]

    try:
        # mandatory fields
        reference_data = {field: request.form.get(field) for field in mandatory_fields}
        for field, value in reference_data.items():
            if not value:
                raise ValueError(f"Missing mandatory field: {field}")

        # optional fields
        reference_data.update({field: request.form.get(field) or None for field in optional_fields})

        # create a References object using keyword arguments
        reference = References(
            id=None,          # id is managed by db
            created_at=None,  # created_at not needed here
            **reference_data  # unpack dictionary to arguments
        )

        # validate reference
        validate_reference(reference)

        # store reference to db
        create_reference(reference)

        flash("Added succesfully")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_reference")


# When user clicks download button, get references as string and download as .bib file
@app.route("/download")
def getBibtexFile():
    references = get_references()
    bibtex_str = reference_bibtex_parser(references)

    if not bibtex_str:
        flash("There are no references to download.")
        return redirect("/")
    return Response(
        bibtex_str,
        mimetype="text/plain",
        headers={"Content-disposition": "attachment; filename=references.bib"},
    )


# testausta varten oleva reitti
if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({"message": "db reset"})

    if populate_env:
        with app.app_context():
            reset_db()
            populate_database()
