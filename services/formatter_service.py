def format_customer_summary(data):

    if data is None:

        return "Customer not found."

    text = []

    text.append(
        f"Customer : {data['firstname']} {data['lastname']}"
    )

    text.append(
        f"Account : {data['account_no']}"
    )

    text.append(
        f"Status : {data['status']}"
    )

    text.append(
        f"Balance : ₱{data['balance']:.2f}"
    )

    text.append("")

    text.append("Recent Payments:")

    if data["payments"]:

        for payment in data["payments"]:

            text.append(
                f"- {payment['payment_date']} : ₱{payment['amount']}"
            )

    else:

        text.append("- None")

    text.append("")

    text.append(
        f"Open Tickets : {len(data['open_tickets'])}"
    )

    text.append(
        f"Pending Requests : {len(data['pending_requests'])}"
    )

    text.append(
        f"Unpaid Invoices : {len(data['unpaid_invoices'])}"
    )

    return "\n".join(text)