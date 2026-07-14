from tools.register import registry

customer = registry.execute(

    "customer_profile",

    "100001"

)

print(customer)