from database.repositories.ticket_repository import TicketRepository


repository = TicketRepository()


def get_ticket_summary(account_no):
    """
    Returns all open tickets for a customer.
    """

    return repository.get_open(account_no)