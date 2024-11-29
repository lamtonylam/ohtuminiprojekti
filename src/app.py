from flask import redirect, render_template, request, jsonify, flash, Response
from db_helper import reset_db
from repositories.inproceedings_repository import get_inproceedings, create_reference
from config import app, test_env, populate_env
from util import validate_book, validate_article, validate_inproceedings
from populate_test_data import populate_database
from bibtex_parser import inproceeding_bibtex_parser


@app.route("/")
def index():
    inproceedings = get_inproceedings()
    return render_template("index.html", inproceedings=inproceedings)


# get a preview of the bibtex
@app.route("/preview")
def bibtexpreview():
    inproceedings = get_inproceedings()
    return render_template(
        "preview.html", inproceedings_list_bibtex=inproceeding_bibtex_parser(inproceedings)
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
    booktitle = request.form.get("booktitle")
    year = request.form.get("year")

    # optional fields
    editor = request.form.get("editor") or None
    volume = request.form.get("volume") or None
    number = request.form.get("number") or None
    series = request.form.get("series") or None

    reference_type = "book"
    journal = "Life"
    note = "Hello world"

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
                note
            )

        elif reference_type == "book":
            validate_book(
                author,
                year,
                title,
                publisher,
                address
            )
            
        elif reference_type == "inproceedings":
            validate_inproceedings(
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
                publisher
            )

        # Inputs given as arguments to the validation function //found in util.py
        create_reference(
            reference_id,
            reference_type,
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
        )
        flash("Added succesfully")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_reference")


# When user clicks download button, get references as string and download as .bib file
@app.route("/download")
def getBibtexFile():
    inproceedings = get_inproceedings()
    bibtex_str = inproceeding_bibtex_parser(inproceedings)

    if not bibtex_str:
        flash("There are no references to download.")
        return redirect("/")
    return Response(
        bibtex_str,
        mimetype="text/plain",
        headers={'Content-disposition': 'attachment; filename=references.bib'}
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
