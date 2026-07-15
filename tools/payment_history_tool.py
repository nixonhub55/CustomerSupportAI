from tools.base_tool import BaseTool
from services.payment_service import get_payment_history


class PaymentHistoryTool(BaseTool):

    AUTO_REGISTER = True

    NAME = "payment_history"

    DISPLAY_NAME = "Payment History"

    DESCRIPTION = "Retrieve recent payment history."

    CATEGORY = "tool"

    PLUGIN = "billing"

    PARAMETERS = [
        {
            "name": "account_no",
            "type": "string",
            "required": True,
            "description": "Customer account number"
        }
    ]

    def execute(self, account_no):

        return get_payment_history(account_no)