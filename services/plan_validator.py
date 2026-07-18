from core.logger import Logger


REQUIRES_ACCOUNT = {

    "customer_lookup",
    "payment_history",
    "invoice_summary",
    "ticket_summary"

}


def validate(execution_plan):

    Logger.debug("Validating execution plan...")

    errors = []

    for step in execution_plan.steps:

        tool = step["tool"]

        args = step["arguments"]

        if tool in REQUIRES_ACCOUNT:

            if not args.get("account_no"):

                errors.append(
                    f"{tool} requires account_no"
                )

    Logger.debug(
        f"Validation errors: {errors}"
    )

    return errors