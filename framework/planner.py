import re


class Planner:

    def create_plan(self, question):

        q = question.lower()

        account_no = None

        match = re.search(r"\b\d{6,12}\b", q)

        if match:
            account_no = match.group()

        plan = []

        if any(word in q for word in [
            "customer",
            "account",
            "balance",
            "status",
            "plan"
        ]):

            plan.append({
                "tool": "customer_lookup",
                "args": {
                    "account_no": account_no
                }
            })

        if "invoice" in q or "bill" in q:

            plan.append({
                "tool": "invoice_summary",
                "args": {
                    "account_no": account_no
                }
            })

        if "payment" in q:

            plan.append({
                "tool": "payment_history",
                "args": {
                    "account_no": account_no
                }
            })

        if "ticket" in q or "support" in q:

            plan.append({
                "tool": "ticket_summary",
                "args": {
                    "account_no": account_no
                }
            })

        return plan