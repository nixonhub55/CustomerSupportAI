from tools.base_tool import BaseTool

from services.payment_service import get_payment_history


class PaymentHistoryTool(BaseTool):

    def execute(self, account_no):

        return get_payment_history(
            account_no
        )