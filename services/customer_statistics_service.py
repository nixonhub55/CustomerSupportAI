from database.repositories.customer_repository import CustomerRepository


def get_customer_statistics():

    repository = CustomerRepository()

    return {
        "total_customers": repository.count()
    }