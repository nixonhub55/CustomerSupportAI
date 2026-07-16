import re

from framework.execution_plan import ExecutionPlan


def plan(question):

    question = question.lower()

    execution_plan = ExecutionPlan()

    # -----------------------------------------
    # Detect account number
    # -----------------------------------------

    account_match = re.search(
        r"\b\d{6,12}\b",
        question
    )

    account_no = None

    if account_match:
        account_no = account_match.group()

    # -----------------------------------------
    # Customer lookup
    # -----------------------------------------

    if (
        "customer" in question
        or "account" in question
        or account_no
    ):

        execution_plan.add(
            "customer_lookup",
            account_no=account_no
        )

    # -----------------------------------------
    # Payment history
    # -----------------------------------------

    if (
        "payment" in question
        or "paid" in question
        or "history" in question
    ):

        execution_plan.add(
            "payment_history",
            account_no=account_no
        )

    # -----------------------------------------
    # Invoice summary
    # -----------------------------------------

    if (
        "invoice" in question
        or "bill" in question
        or "balance" in question
    ):

        execution_plan.add(
            "invoice_summary",
            account_no=account_no
        )

    # -----------------------------------------
    # Ticket summary
    # -----------------------------------------

    if (
        "ticket" in question
        or "tickets" in question
        or "case" in question
        or "complaint" in question
    ):

        execution_plan.add(
            "ticket_summary",
            account_no=account_no
        )

    # -----------------------------------------
    # Customer statistics
    # -----------------------------------------

    if (
        "how many" in question
        or "count" in question
        or "number of customers" in question
        or "total customers" in question
    ):

        execution_plan.add(
            "customer_statistics"
        )

    return execution_plan