from database.connection import connect


class KnowledgeRepository:

    def search(self, keyword):

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM knowledge
            WHERE status=1
            AND (
                title LIKE ?
                OR keywords LIKE ?
                OR content LIKE ?
            )
        """, (

            f"%{keyword}%",

            f"%{keyword}%",

            f"%{keyword}%"

        ))

        rows = cursor.fetchall()

        cursor.close()

        conn.close()

        return rows