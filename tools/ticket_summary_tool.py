from tools.base_tool import BaseTool
from services.ticket_service import get_ticket_summary


class TicketSummaryTool(BaseTool):

    name = "ticket_summary"

    description = "Retrieve open support tickets."

    category = "support"

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

        return get_ticket_summary(account_no)