from framework.framework import Framework

framework = Framework()

framework.start()

customer = framework.tools.execute(
    "customer.profile",
    "100001"
)

print(customer)