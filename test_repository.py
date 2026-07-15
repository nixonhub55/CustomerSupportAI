from services.customer_service import get_customer_profile

customer = get_customer_profile(
    account_no="100001"
)

print(customer)