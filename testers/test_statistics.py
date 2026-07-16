from framework.tool_registry import ToolRegistry

from tools.customer_statistics_tool import (
    CustomerStatisticsTool
)

registry = ToolRegistry()

registry.register(
    CustomerStatisticsTool()
)

print(
    registry.execute(
        "customer_statistics"
    )
)