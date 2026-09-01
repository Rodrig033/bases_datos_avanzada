import os

import ZODB
import ZODB.FileStorage


DATABASE_PATH = os.path.join(
    "data",
    "biblioteca.fs"
)


def abrir_base_datos():

    storage = ZODB.FileStorage.FileStorage(
        DATABASE_PATH
    )

    db = ZODB.DB(storage)

    connection = db.open()

    root = connection.root()

    return db, connection, root