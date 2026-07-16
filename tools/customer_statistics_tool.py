from tools.base_tool import BaseTool
from services.customer_service import count_customers


class CustomerStatisticsTool(BaseTool):

    AUTO_REGISTER = True

    NAME = "customer_statistics"

    DISPLAY_NAME = "Customer Statistics"

    DESCRIPTION = "Retrieve customer statistics."

    CATEGORY = "tool"

    PLUGIN = "core"

    PARAMETERS = [
        {
            "name": "filters",
            "type": "object",
            "required": False
        }
    ]

    def execute(self, **kwargs):

        total = count_customers(**kwargs)

        return {
            "total_customers": total
        }