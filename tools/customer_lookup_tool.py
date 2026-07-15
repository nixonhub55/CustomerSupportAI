from tools.base_tool import BaseTool
from services.customer_service import get_customer_profile


class CustomerLookupTool(BaseTool):

    name = "customer_lookup"

    description = "Retrieve customer profile information."

    parameters = [
        {
            "name": "filters",
            "type": "object",
            "required": False
        }
    ]

    category = "general"

    plugin = "core"

    def execute(self, **kwargs):
        """
        Retrieve a customer using any supported filter.
        """
        return get_customer_profile(**kwargs)