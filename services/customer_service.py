from database.repositories.customer_repository import CustomerRepository
from constants import STATUS_MAP

repository = CustomerRepository()


def get_customer_profile(account_no):

    customer = repository.get_by_account(account_no)

    if customer is None:
        return None

    return {
        "account_no": customer["account_no"],
        "fullname": f"{customer['firstname']} {customer['middlename']} {customer['lastname']}".replace("  ", " ").strip(),
        "status": STATUS_MAP.get(customer["status"], "Unknown"),
        "plan": customer["plan"],
        "balance": customer["balance"],
        "phone": customer.get("phone"),
        "email": customer.get("email"),
        "address": customer.get("address"),
    }