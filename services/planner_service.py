import re

from framework.execution_plan import ExecutionPlan


def plan(question):

    question = question.lower()

    execution_plan = ExecutionPlan()

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
    # Customer statistics
    # -----------------------------------------

    if (
        "how many" in question
        or "count" in question
        or "total customers" in question
        or "number of customers" in question
    ):

        execution_plan.add(
            "customer_statistics"
        )

    return execution_plan