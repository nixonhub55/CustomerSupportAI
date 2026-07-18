from core.logger import Logger
from framework.execution_plan import ExecutionPlan 
from services.normalizer import normalize
from services.intent_detector import detect_intent
from services.text_utils import (
    contains_any,
    extract_account_no,
)


def plan(question):

    # -----------------------------------------
    # Normalize
    # -----------------------------------------

    question = normalize(question)

    Logger.debug(f"Normalized question: {question}")

    question_lower = question

    Logger.info(
        f"Planning: {question}"
    )

    execution_plan = ExecutionPlan()

    # -----------------------------------------
    # Detect Intent
    # -----------------------------------------

    execution_plan.intent = detect_intent(question)

    if execution_plan.intent != "customer_support":

        Logger.debug(
            f"Intent: {execution_plan.intent}"
        )

        return execution_plan

    # -----------------------------------------
    # Detect Account Number
    # -----------------------------------------

    account_no = extract_account_no(question_lower)

    Logger.debug(f"Extracted account_no: {account_no}")

    # -----------------------------------------
    # Customer Lookup
    # -----------------------------------------

    if (
        "customer" in question_lower
        or "account" in question_lower
        or account_no
    ):

        execution_plan.add_step(
            "customer_lookup",
            account_no=account_no
        )

    # -----------------------------------------
    # Customer Profile Questions
    # -----------------------------------------

    if contains_any(question_lower, [

        "active",
        "inactive",

        "status",

        "phone",
        "mobile",
        "contact",

        "email",

        "address",

        "plan",

        "name",

    ]):

        execution_plan.add_step(
            "customer_lookup",
            account_no=account_no
        )

    # -----------------------------------------
    # Customer List
    # -----------------------------------------

    if contains_any(question_lower, [

        "all customers",
        "list customers",
        "show customers",
        "customer list",
        "all customer",
        "all account"

    ]):

        execution_plan.add_step(
            "customer_list"
        )

    # -----------------------------------------
    # Payment History
    # -----------------------------------------

    Logger.debug(
        f"Payment detection: {question_lower}"
    )

    if contains_any(question_lower, [
        
        "payment",
        "paid",
        "history"

    ]):

        Logger.debug(
            "Planner decided to execute payment_history."
        )

        execution_plan.add_step(
            "payment_history",
            account_no=account_no
        )

    # -----------------------------------------
    # Invoice Summary
    # -----------------------------------------

    if contains_any(question_lower, [

        "invoice",
        "bill",
        "balance"

    ]):

        execution_plan.add_step(
            "invoice_summary",
            account_no=account_no
        )

    # -----------------------------------------
    # Ticket Summary
    # -----------------------------------------

    if contains_any(question_lower, [

        "ticket",
        "tickets",
        "case",
        "complaint"

    ]):

        execution_plan.add_step(
            "ticket_summary",
            account_no=account_no
        )

    # -----------------------------------------
    # Customer Statistics
    # -----------------------------------------

    if contains_any(question_lower, [

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