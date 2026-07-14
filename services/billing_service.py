from database.repositories.customer_repository import CustomerRepository
from database.repositories.payment_repository import PaymentRepository
from database.repositories.invoice_repository import InvoiceRepository
from database.repositories.ticket_repository import TicketRepository
from database.repositories.service_request_repository import ServiceRequestRepository

from constants import STATUS_MAP


class BillingService:

    def __init__(self):

        self.customer_repo = CustomerRepository()

        self.payment_repo = PaymentRepository()

        self.invoice_repo = InvoiceRepository()

        self.ticket_repo = TicketRepository()

        self.service_repo = ServiceRequestRepository()

    def get_customer_summary(self, account_no):

        customer = self.customer_repo.get_by_account(account_no)

        if customer is None:

            return None

        customer["status"] = STATUS_MAP.get(
            customer["status"],
            "Unknown"
        )

        customer["payments"] = self.payment_repo.get_recent(
            account_no
        )

        customer["unpaid_invoices"] = self.invoice_repo.get_unpaid(
            account_no
        )

        customer["open_tickets"] = self.ticket_repo.get_open(
            account_no
        )

        customer["pending_requests"] = self.service_repo.get_pending(
            account_no
        )

        return customer