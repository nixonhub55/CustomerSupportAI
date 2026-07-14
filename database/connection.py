import mariadb
from config import *


def connect():
    return mariadb.connect(
        host="localhost",
        user="root",
        password="PfNgB@y@n",
        database="billing_db"
    )