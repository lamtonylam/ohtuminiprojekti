from config import db
from sqlalchemy import text

from entities.inproceedings import Inproceedings


def get_inproceedings():
    result = db.session.execute(
        text("""
            SELECT reference_id, reference_type, title, author, year, publisher, address, journal, volume, 
                number, pages, month, note, booktitle, editor, series, organization
            FROM reference
        """)
    )
    inproceedings_result = result.fetchall()
    return [
        Inproceedings(
            inproceeding[0],
            inproceeding[1],
            inproceeding[2],
            inproceeding[3],
            inproceeding[4],
            inproceeding[5],
            inproceeding[6],
            inproceeding[7],
            inproceeding[8],
            inproceeding[9],
            inproceeding[10],
            inproceeding[11],
            inproceeding[12],
            inproceeding[13],
            inproceeding[14],
            inproceeding[15],
        )
        for inproceeding in inproceedings_result
    ]


def create_reference(
    reference_id,
    reference_type,
    title,
    author,
    year,
    booktitle=None,
    editor=None,
    volume=None,
    number=None,
    series=None,
    pages=None,
    address=None,
    journal=None,
    month=None,
    note=None,
    organization=None,
    publisher=None,
):
    sql = text(
        """INSERT INTO reference (reference_id, reference_type, title, author, year, publisher, address, journal, volume, 
                number, pages, month, note, booktitle, editor, series, organization) 
                VALUES (:reference_id, :reference_type, :title, :author, :year, :publisher, :address, :journal, :volume, 
                :number, :pages, :month, :note, :booktitle, :editor, :series, :organization)"""
    )
    db.session.execute(
        sql,
        {
            "reference_id": reference_id,
            "reference_type": reference_type,
            "title": title,
            "author": author,
            "year": int(year),
            "publisher": publisher,
            "address": address,
            "journal": journal,
            "volume": volume,
            "number": number,
            "pages": pages,
            "month": month,
            "note": note,
            "booktitle": booktitle,
            "editor": editor,
            "series": series,
            "organization": organization
        },
    )
    db.session.commit()
