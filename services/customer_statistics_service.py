from database.customer_db import CUSTOMERS


def get_customer_statistics():

    return {
        "total_customers": len(CUSTOMERS)
    }