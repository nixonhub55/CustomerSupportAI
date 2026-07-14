from tools.base_tool import BaseTool
from services.payment_service import get_payment_history


class PaymentHistoryTool(BaseTool):

    name = "payment_history"

    description = "Retrieve recent payment history."

    category = "payment"

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

        return get_payment_history(account_no)