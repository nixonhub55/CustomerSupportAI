import re
from core.logger import Logger
from framework.execution_plan import ExecutionPlan



def plan(question):
    
    Logger.info(
        f"Planning: {question}"
    ) 

    question_lower = question.lower()

    execution_plan = ExecutionPlan()

    # -------------------------------------------------
    # Detect Intent
    # -------------------------------------------------

    if any(word in question_lower for word in [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]):

        execution_plan.intent = "greeting"

        return execution_plan

    if any(word in question_lower for word in [
        "thanks",
        "thank you",
        "thank u"
    ]):

        execution_plan.intent = "gratitude"

        return execution_plan

    if any(word in question_lower for word in [
        "bye",
        "goodbye",
        "see you"
    ]):

        execution_plan.intent = "farewell"

        return execution_plan

    # -------------------------------------------------
    # Default intent
    # -------------------------------------------------

    execution_plan.intent = "customer_support"

    # -------------------------------------------------
    # Detect Account Number
    # -------------------------------------------------

    account_match = re.search(
        r"\b\d{6,12}\b",
        question_lower
    )

    account_no = None

    if account_match:
        account_no = account_match.group()

    # -------------------------------------------------
    # Customer Lookup
    # -------------------------------------------------

    if (
        "customer" in question_lower
        or "account" in question_lower
        or account_no
    ):

        execution_plan.add_step(
            "customer_lookup",
            account_no=account_no
        )
    
    if (
        "all customers" in question_lower
        or "list customers" in question_lower
        or "show customers" in question_lower
        or "customer list" in question_lower
        or "all customer" in question_lower
        or "all account" in question_lower
    ):

        execution_plan.add_step(
            "customer_list"
        )

    # -------------------------------------------------
    # Payment History
    # -------------------------------------------------

    if any(word in question_lower for word in [
        "payment",
        "paid",
        "history"
    ]):

        execution_plan.add_step(
            "payment_history",
            account_no=account_no
        )

    # -------------------------------------------------
    # Invoice Summary
    # -------------------------------------------------

    if any(word in question_lower for word in [
        "invoice",
        "bill",
        "balance"
    ]):

        execution_plan.add_step(
            "invoice_summary",
            account_no=account_no
        )

    # -------------------------------------------------
    # Ticket Summary
    # -------------------------------------------------

    if any(word in question_lower for word in [
        "ticket",
        "tickets",
        "case",
        "complaint"
    ]):

        execution_plan.add_step(
            "ticket_summary",
            account_no=account_no
        )

    # -------------------------------------------------
    # Customer Statistics
    # -------------------------------------------------

    if any(word in question_lower for word in [
        "how many",
        "count",
        "number of customers",
        "total customers"
    ]):

        execution_plan.add_step(
            "customer_statistics"
        )


    Logger.debug(
        f"Intent: {execution_plan.intent}"
    )

    Logger.debug(
        f"Steps: {execution_plan.steps}"
    )


    return execution_plan