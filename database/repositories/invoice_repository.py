from database.connection import connect


class InvoiceRepository:

    def get_unpaid(self, account_no):

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM invoices
            WHERE account_no=?
            AND status='UNPAID'
            ORDER BY due_date
        """, (account_no,))

        invoices = cursor.fetchall()

        cursor.close()

        conn.close()

        return invoices