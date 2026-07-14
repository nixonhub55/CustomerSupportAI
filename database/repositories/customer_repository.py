from database.connection import connect


class CustomerRepository:

    def get_by_account(self, account_no):

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
                balance,
                phone,
                email,
                address
            FROM customers
            WHERE account_no = ?
        """, (account_no,))

        customer = cursor.fetchone()

        cursor.close()
        conn.close()

        return customer