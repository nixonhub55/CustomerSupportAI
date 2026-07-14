from database.connection import connect


class ServiceRequestRepository:

    def get_pending(self, account_no):

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM service_requests
            WHERE account_no=?
            AND status IN ('PENDING','APPROVED','ONGOING')
        """, (account_no,))

        requests = cursor.fetchall()

        cursor.close()

        conn.close()

        return requests