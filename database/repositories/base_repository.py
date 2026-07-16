from database.connection import connect
from core.base_component import BaseComponent
from core.logger import Logger

class BaseRepository(BaseComponent):

    TABLE = None

    PRIMARY_KEY = None

    SEARCHABLE_FIELDS = set() 

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

        Logger.debug(sql)

        Logger.debug(
            f"Parameters: {values}"
        )

        cursor.execute(sql, tuple(values))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    def metadata(self):

        data = super().metadata()

        data.update({
            "table": self.TABLE,
            "primary_key": self.PRIMARY_KEY,
            "searchable_fields": sorted(
                self.SEARCHABLE_FIELDS
            ),
            "default_order": self.DEFAULT_ORDER
        })

        return data

    def count(self, **filters):

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

        sql = f"SELECT COUNT(*) AS total FROM {self.TABLE}"

        if clauses:
            sql += " WHERE " + " AND ".join(clauses)

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        Logger.debug(sql)

        Logger.debug(
            f"Parameters: {values}"
        )

        cursor.execute(sql, tuple(values))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row["total"]

    def exists(self, **filters):

        return self.count(**filters) > 0

    def find_all(self, **filters):

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

        sql = f"""
            SELECT *
            FROM {self.TABLE}
        """

        if clauses:
            sql += " WHERE " + " AND ".join(clauses)

        if self.DEFAULT_ORDER:
            sql += f" ORDER BY {self.DEFAULT_ORDER}"

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        Logger.debug(sql)

        Logger.debug(
            f"Parameters: {values}"
        )

        cursor.execute(sql, tuple(values))

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    def search(self, keyword):

        if self.TABLE is None:
            raise NotImplementedError(
                "TABLE must be defined."
            )

        clauses = []
        values = []

        for field in self.SEARCHABLE_FIELDS:

            clauses.append(f"{field} LIKE ?")

            values.append(f"%{keyword}%")

        sql = f"""
            SELECT *
            FROM {self.TABLE}
            WHERE {' OR '.join(clauses)}
        """

        if self.DEFAULT_ORDER:
            sql += f" ORDER BY {self.DEFAULT_ORDER}"

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        Logger.debug(sql)

        Logger.debug(
            f"Parameters: {values}"
        )

        cursor.execute(sql, tuple(values))

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows