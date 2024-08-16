#MANY
import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Pepin"),
        (3, "Pepon")
    ]
    cursor.executemany(
        "insert into usuarios values(?,?)",
        usuarios,
    )