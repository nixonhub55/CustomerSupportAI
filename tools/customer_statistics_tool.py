from tools.base_tool import BaseTool
from services.customer_statistics_service import (
    get_customer_statistics
)


class CustomerStatisticsTool(BaseTool):

    AUTO_REGISTER = True

    NAME = "customer_statistics"

    DISPLAY_NAME = "Customer Statistics"

    DESCRIPTION = "Returns customer statistics."

    CATEGORY = "tool"

    PLUGIN = "core"

    PARAMETERS = []

    KEYWORDS = [

        "count",
        "how many",
        "statistics",
        "total customers"

    ]

    def execute(self):

        return get_customer_statistics()