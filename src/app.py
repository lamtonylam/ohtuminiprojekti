from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.inproceedings_repository import get_inproceedings, create_inproceeding
from config import app, test_env, populate_env
from util import validate_inproceeding
from populate_test_data import populate_database


@app.route("/")
def index():
    inproceedings = get_inproceedings()
    # return render_template("index.html", todos=todos, unfinished=unfinished)
    return render_template("index.html", inproceedings=inproceedings)


@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/preview")
def preview():
    return render_template("preview.html")


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
    pages = request.form.get("pages") or None
    address = request.form.get("address") or None
    month = request.form.get("month") or None
    organization = request.form.get("organization") or None
    publisher = request.form.get("publisher") or None

    try:
        # Inputs given as arguments to the validation function //found in util.py
        validate_inproceeding(reference_id, author, title, booktitle, year, editor, volume, number, series, pages, address, month, organization, publisher)
        create_inproceeding(reference_id, author, title, booktitle, year, editor, volume, number, series, pages, address, month, organization, publisher)
        flash("Added succesfully")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_reference")


@app.route("/download", methods=["POST"])
def download():
    flash("Function is not ready")
    return redirect("/")



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
