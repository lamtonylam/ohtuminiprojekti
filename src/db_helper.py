from sqlalchemy import text
from config import db, app

table_name = "reference"


def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]


def reset_db():
    print(f"Clearing contents from table {table_name}")
    sql = text(f"DELETE FROM {table_name}")
    db.session.execute(sql)
    db.session.commit()

    print(f"Resetting the serialization of table {table_name}")
    sql_reset_serial = text(f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1")
    db.session.execute(sql_reset_serial)
    db.session.commit()


def setup_db():
    if table_exists(table_name):
        print(f"Table {table_name} exists, dropping")
        sql = text(f"DROP TABLE {table_name}")
        db.session.execute(sql)
        db.session.commit()

    with open("./src/schema.sql", "r", encoding="utf-8") as schema:
        sql = text(schema.read())

    print(f"Creating table {table_name}")

    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
