from database.connection import connect


class TicketRepository:

    def get_open(self, account_no):

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM tickets
            WHERE account_no=?
            AND status IN ('OPEN','IN_PROGRESS')
        """, (account_no,))

        tickets = cursor.fetchall()

        cursor.close()

        conn.close()

        return tickets