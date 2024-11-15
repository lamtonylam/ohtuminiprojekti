from config import db
from sqlalchemy import text

from entities.inproceedings import Inproceedings


def get_inproceedings():
    result = db.session.execute(
        text(
            "SELECT id, reference_id, created_at, author, title, booktitle, year, editor, volume, number, series, pages, address, month, organization, publisher FROM inproceedings"
        )
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


def create_inproceeding(
    reference_id,
    author,
    title,
    booktitle,
    year,
    editor=None,
    volume=None,
    number=None,
    series=None,
    pages=None,
    address=None,
    month=None,
    organization=None,
    publisher=None,
):
    sql = text(
        """INSERT INTO inproceedings (reference_id, author, title, booktitle, year, 
                editor, volume, number, series, pages, address, month, organization, publisher) 
                VALUES (:reference_id, :author, :title, :booktitle, :year, :editor, :volume, 
                :number, :series, :pages, :address, :month, :organization, :publisher)"""
    )
    print(sql)
    db.session.execute(
        sql,
        {
            "reference_id": reference_id,
            "author": author,
            "title": title,
            "booktitle": booktitle,
            "year": int(year),
            "editor": editor,
            "volume": volume,
            "number": number,
            "series": series,
            "pages": pages,
            "address": address,
            "month": month,
            "organization": organization,
            "publisher": publisher,
        },
    )
    db.session.commit()
