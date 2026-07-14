from framework.tool_registry import ToolRegistry

from tools.customer_lookup_tool import CustomerLookupTool

registry = ToolRegistry()

registry.register(CustomerLookupTool())

customer = registry.execute(

    "customer_lookup",

    account_no="100001"

)

print(customer)