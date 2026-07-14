from database.repositories.payment_repository import PaymentRepository


repository = PaymentRepository()


def get_payment_history(account_no, limit=10):
    """
    Returns the recent payment history for a customer.
    """

    return repository.get_recent(
        account_no,
        limit
    )