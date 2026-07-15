from database.connection import connect
 
    

class CustomerRepository:


    SEARCHABLE_FIELDS = {
        "account_no",
        "phone",
        "email",
        "firstname",
        "lastname",
        "middlename" 
    }

    def find_one(self, **filters):
    
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
            FROM customers
            WHERE {' AND '.join(clauses)}
            LIMIT 1
        """

        conn = connect()

        cursor = conn.cursor(dictionary=True)

        cursor.execute(sql, tuple(values))

        customer = cursor.fetchone()

        cursor.close()
        conn.close()

        return customer