from database.repositories.customer_repository import CustomerRepository


def get_customer_list(**filters):

    repository = CustomerRepository()

    return repository.find_all(**filters)