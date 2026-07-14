from database.repositories.customer_repository import CustomerRepository

repo = CustomerRepository()

customer = repo.get_by_account("100001")

print(customer)