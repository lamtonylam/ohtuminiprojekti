from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.inproceedings_repository import get_inproceedings, create_inproceeding
from config import app, test_env
from util import validate_inproceeding


@app.route("/")
def index():
    inproceedings = get_inproceedings()
    # return render_template("index.html", todos=todos, unfinished=unfinished)
    return render_template("index.html", inproceedings=inproceedings)


@app.route("/new_todo")
def new():
    return render_template("new_todo.html")


@app.route("/create_todo", methods=["POST"])
def todo_creation():
    reference_id = request.form.get("reference_id")
    author = request.form.get("author")
    title = request.form.get("title")
    booktitle = request.form.get("booktitle")
    year = request.form.get("year")

    editor = request.form.get("editor")
    editor = None if editor == "" else editor
    volume = request.form.get("volume")
    volume = None if volume == "" else volume
    number = request.form.get("number")
    number = None if number == "" else number
    series = request.form.get("series")
    series = None if series == "" else series
    pages = request.form.get("pages")
    pages = None if pages == "" else pages
    address = request.form.get("address")
    address = None if address == "" else address
    month = request.form.get("month")
    month = None if month == "" else month
    organization = request.form.get("organization")
    organization = None if organization == "" else organization
    publisher = request.form.get("publisher")
    publisher = None if publisher == "" else publisher

    try:
        validate_inproceeding(reference_id, author, title, booktitle, year)
        create_inproceeding(
            reference_id=reference_id,
            author=author,
            title=title,
            booktitle=booktitle,
            year=year,
            editor=editor,
            volume=volume,
            number=number,
            series=series,
            pages=pages,
            address=address,
            month=month,
            organization=organization,
            publisher=publisher,
        )
        flash(str("Added succesfully"))
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_todo")


# testausta varten oleva reitti
if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({"message": "db reset"})
