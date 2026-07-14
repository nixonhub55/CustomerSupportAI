from tools.base_tool import BaseTool

from services.ticket_service import get_ticket_summary


class TicketSummaryTool(BaseTool):

    def execute(self, account_no):

        return get_ticket_summary(
            account_no
        )