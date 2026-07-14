from tools.base_tool import BaseTool

from database.repositories.payment_repository import PaymentRepository


class PaymentHistoryTool(BaseTool):

    name = "payment_history"

    description = "Returns payment history."

    def __init__(self):

        self.repo = PaymentRepository()

    def execute(self, account_no):

        return self.repo.get_recent(account_no)