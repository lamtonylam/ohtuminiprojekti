from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from repositories.references_repository import get_references, create_reference
from config import app, test_env, populate_env
from validate import validate_book, validate_article, validate_inproceedings
from populate_test_data import populate_database
from bibtex_parser import reference_bibtex_parser


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
    # mandatory fields
    reference_id = request.form.get("reference_id")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    reference_type = request.form.get("reference_type")
    print(reference_type)

    # optional fields
    booktitle = request.form.get("booktitle") or None
    editor = request.form.get("editor") or None
    volume = request.form.get("volume") or None
    number = request.form.get("number") or None
    series = request.form.get("series") or None

    # reference_type = "book"
    journal = request.form.get("journal") or None
    note = request.form.get("note") or None
    pages = request.form.get("pages") or None
    address = request.form.get("address") or None
    month = request.form.get("month") or None
    organization = request.form.get("organization") or None
    publisher = request.form.get("publisher") or None

    try:
        if reference_type == "article":
            validate_article(
                reference_id,
                author,
                title,
                journal,
                year,
                volume,
                number,
                pages,
                month,
                note,
            )

        elif reference_type == "book":
            validate_book(reference_id, author, year, title, publisher, address)

        elif reference_type == "inproceedings":
            validate_inproceedings(
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
            )

        # Inputs given as arguments to the validation function //found in validate.py
        create_reference(
            reference_id,
            reference_type,
            author,
            title,
            year,
            booktitle,
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
            note,
        )
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
