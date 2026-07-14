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


def get_customer(account_no):

    conn = connect()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            account_no,
            lastname,
            firstname,
            middlename,
            status,
            plan,
            balance
        FROM customers
        WHERE account_no = ?
    """, (account_no,))

    customer = cursor.fetchone()

    cursor.close()
    conn.close()

    return customer