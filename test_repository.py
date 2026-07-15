from services.customer_service import get_customer_profile

customer = get_customer_profile(
    phone="0922233322"
)

print(customer)