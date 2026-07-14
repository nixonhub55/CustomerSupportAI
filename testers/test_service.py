from services.database_service import get_customer_profile

customer = get_customer_profile("100001")

print(customer)