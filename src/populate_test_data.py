from config import db
from test_data import test_data
from sqlalchemy import text


table_name = "inproceedings"

def populate_database():
    sql = text(f"""
            INSERT INTO {table_name} (
                reference_id, author, title, booktitle, year, editor, volume, number, 
                series, pages, address, month, organization, publisher
            )
            VALUES (
                :reference_id, :author, :title, :booktitle, :year, :editor, :volume, :number, 
                :series, :pages, :address, :month, :organization, :publisher
            )
        """)

    for row in test_data:
        db.session.execute(sql, row)

    db.session.commit()
