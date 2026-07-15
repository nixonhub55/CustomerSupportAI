from tools.base_tool import BaseTool
from services.customer_service import get_customer_profile


class CustomerLookupTool(BaseTool):

    AUTO_REGISTER = True

    NAME = "customer_lookup"

    DISPLAY_NAME = "Customer Lookup"

    DESCRIPTION = "Retrieve customer profile information."

    CATEGORY = "tool"

    PARAMETERS = [
        {
            "name": "filters",
            "type": "object",
            "required": False
        }
    ]

    PLUGIN = "core"

    def execute(self, **kwargs):
        """
        Retrieve a customer using any supported filter.
        """
        return get_customer_profile(**kwargs)