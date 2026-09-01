import os

import ZODB
import ZODB.FileStorage


DATABASE_PATH = os.path.join("data", "universidad.fs")


def abrir_base_datos():
    """Abre la base de datos y devuelve DB, conexión y root."""

    storage = ZODB.FileStorage.FileStorage(DATABASE_PATH)

    db = ZODB.DB(storage)

    connection = db.open()

    root = connection.root()

    return db, connection, root