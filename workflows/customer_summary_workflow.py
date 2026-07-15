from core.base_workflow import BaseWorkflow


class CustomerSummaryWorkflow(BaseWorkflow):

    AUTO_REGISTER = True

    NAME = "customer_summary"

    DISPLAY_NAME = "Customer Summary"

    DESCRIPTION = "Collect customer information."

    def run(self, context):

        print("Running workflow...")

        return context