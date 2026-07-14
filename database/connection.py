import mariadb
from config import *


def connect():
    return mariadb.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )