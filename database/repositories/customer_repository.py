from database.connection import connect


class CustomerRepository:

    def get_by_account(self, account_no):

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM customers
            WHERE account_no = ?
        """, (account_no,))

        customer = cursor.fetchone()

        cursor.close()
        conn.close()

        return customer