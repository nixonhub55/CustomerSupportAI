from tools.base_tool import BaseTool

from services.billing_service import BillingService


class CustomerLookupTool(BaseTool):

    name = "customer_lookup"

    description = "Returns customer information."

    def __init__(self):

        self.billing = BillingService()

    def execute(self, account_no):

        return self.billing.get_customer_summary(account_no)