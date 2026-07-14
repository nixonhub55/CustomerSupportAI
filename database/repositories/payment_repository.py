from database.connection import connect


class PaymentRepository:

    def get_recent(self, account_no, limit=10):

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM payments
            WHERE account_no = ?
            ORDER BY payment_date DESC
            LIMIT ?
        """, (account_no, limit))

        payments = cursor.fetchall()

        cursor.close()
        conn.close()

        return payments