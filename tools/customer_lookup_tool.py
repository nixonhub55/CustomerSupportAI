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

    KEYWORDS = [ 
            "customer", 
            "account", 
            "subscriber", 
            "profile", 
            "status", 
            "active", 
            "inactive", 
            "plan", 
            "email", 
            "phone", 
            "address", 
            "balance" 
        ]

    EXAMPLES = [

        "Show customer 100001",
        "Customer details",
        "Is customer active?",
        "Who is account 100002?"

    ]

    PLUGIN = "core"

    def execute(self, **kwargs):
        """
        Retrieve a customer using any supported filter.
        """
        return get_customer_profile(**kwargs)