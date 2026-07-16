from database.repositories.customer_repository import CustomerRepository

repository = CustomerRepository()


def get_customer_profile(**filters):
    """
    Returns a customer profile using any searchable field.
    """

    return repository.find_one(**filters)



def count_customers(**filters):

    return repository.count(**filters)