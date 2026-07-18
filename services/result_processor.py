class ResultProcessor:

    def process(self, context):

        if not context:
            return context

        # ----------------------------------------
        # Payment History
        # ----------------------------------------

        payments = context.get("payment_history")

        if payments:

            payment_summary = {

                "last_payment": payments[0],

                "payment_count": len(payments),

                "total_paid": sum(
                    float(payment["amount"])
                    for payment in payments
                )

            }

            context["payment_summary"] = payment_summary

        return context