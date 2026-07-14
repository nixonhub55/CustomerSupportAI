from tools.base_tool import BaseTool
from services.customer_service import get_customer_profile


class CustomerLookupTool(BaseTool):

    name = "customer_lookup"

    description = "Retrieve customer profile by account number."

    category = "customer"

    plugin = "billing"

    parameters = [
        {
            "name": "account_no",
            "type": "string",
            "required": True,
            "description": "Customer account number"
        }
    ]

    def execute(self, account_no):

        return get_customer_profile(account_no)