import os
import ZODB
import ZODB.FileStorage
import transaction

RUTA_BD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "laboratorio.fs")


def abrir_base_datos():
    storage = ZODB.FileStorage.FileStorage(RUTA_BD)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()
    return db, connection, root