from database.connection import connect


class BaseRepository:

    TABLE = None

    PRIMARY_KEY = None

    SEARCHABLE_FIELDS = set()

    DISPLAY_NAME = ""

    DESCRIPTION = ""

    DEFAULT_ORDER = None

    def find_one(self, **filters):

        if self.TABLE is None:
            raise NotImplementedError(
                "TABLE must be defined."
            )

        clauses = []
        values = []

        for field, value in filters.items():

            if value is None:
                continue

            if field not in self.SEARCHABLE_FIELDS:
                raise ValueError(
                    f"Invalid search field: {field}"
                )

            clauses.append(f"{field} = ?")
            values.append(value)

        if not clauses:
            return None

        sql = f"""
            SELECT *
            FROM {self.TABLE}
            WHERE {' AND '.join(clauses)}
            LIMIT 1
        """

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        cursor.execute(sql, tuple(values))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    def metadata(self):

        return {
            "table": self.TABLE,
            "primary_key": self.PRIMARY_KEY,
            "display_name": self.DISPLAY_NAME,
            "description": self.DESCRIPTION,
            "searchable_fields": sorted(
                self.SEARCHABLE_FIELDS
            ),
            "default_order": self.DEFAULT_ORDER,
        }