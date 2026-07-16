from tools.base_tool import BaseTool
from services.ticket_service import get_ticket_summary


class TicketSummaryTool(BaseTool):

    AUTO_REGISTER = True

    NAME = "ticket_summary"

    DISPLAY_NAME = "Ticket Summary"

    DESCRIPTION = "Retrieve open support tickets."

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

        return get_ticket_summary(account_no)