from services.planner_service import plan


class Dispatcher:

    def __init__(self, registry):

        self.registry = registry

    def dispatch(self, assistant, question):

        execution_plan = plan(question)
         
        context = {}

        if execution_plan.get("customer"):

            account_no = execution_plan.get("account_no")

            context["customer_lookup"] = self.registry.execute(
                "customer_lookup",
                account_no=execution_plan.get("account_no"),
                phone=execution_plan.get("phone")
            )

           

        # Knowledge retrieval will be added later.
        # Invoice, payment and ticket retrieval will also
        # be moved here as the planner evolves.

        return context