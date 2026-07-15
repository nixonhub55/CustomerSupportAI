from core.base_capability import BaseCapability


class CustomerCapability(BaseCapability):

    AUTO_REGISTER = True

    NAME = "customer"

    DISPLAY_NAME = "Customer"

    DESCRIPTION = "Customer account capability."

    def can_handle(self, plan):

        return plan.get("customer", False)

    def execute(self, plan):

        print("Customer capability executed.")

        return {}