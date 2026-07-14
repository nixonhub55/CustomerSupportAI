from database.repositories.invoice_repository import InvoiceRepository


repository = InvoiceRepository()


def get_invoice_summary(account_no):
    """
    Returns all unpaid invoices for a customer.
    """

    return repository.get_unpaid(account_no)