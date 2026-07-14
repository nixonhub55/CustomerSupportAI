from database.billing_db import get_customer
from constants import STATUS_MAP


def get_customer_profile(account_no):
    """
    Returns a customer profile formatted for the AI.
    """

    customer = get_customer(account_no)

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


def format_customer(customer):

    if customer is None:
        return "Customer not found."

    return f"""
Account Number : {customer['account_no']}
Customer Name  : {customer['fullname']}
Status         : {customer['status']}
Plan           : {customer['plan']}
Balance        : ₱{customer['balance']:.2f}
Phone          : {customer['phone'] or '-'}
Email          : {customer['email'] or '-'}
Address        : {customer['address'] or '-'}
"""