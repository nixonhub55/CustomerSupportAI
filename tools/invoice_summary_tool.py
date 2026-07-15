from tools.base_tool import BaseTool
from services.invoice_service import get_invoice_summary


class InvoiceSummaryTool(BaseTool):

    AUTO_REGISTER = True

    NAME = "invoice_summary"

    DISPLAY_NAME = "Invoice Summary"

    DESCRIPTION = "Retrieve unpaid invoices."

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

        return get_invoice_summary(account_no)