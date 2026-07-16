from tools.customer_lookup_tool import CustomerLookupTool
from tools.payment_history_tool import PaymentHistoryTool
from tools.invoice_summary_tool import InvoiceSummaryTool
from tools.ticket_summary_tool import TicketSummaryTool
from tools.customer_statistics_tool import CustomerStatisticsTool
from tools.customer_list_tool import CustomerListTool
 

def register_tools(registry):

    registry.register(
        CustomerLookupTool()
    )

    registry.register(
        PaymentHistoryTool()
    )

    registry.register(
        InvoiceSummaryTool()
    )

    registry.register(
        TicketSummaryTool()
    )

    registry.register(
        CustomerStatisticsTool()
    )

    registry.register(
        CustomerListTool()
    )
    