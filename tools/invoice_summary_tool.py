from tools.base_tool import BaseTool
from services.invoice_service import get_invoice_summary


class InvoiceSummaryTool(BaseTool):

    name = "invoice_summary"
    description = "Retrieve unpaid invoices."

    def execute(self, account_no):
        return get_invoice_summary(account_no)