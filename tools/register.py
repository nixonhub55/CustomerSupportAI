from core.tool_registry import ToolRegistry

from tools.customer_tools import customer_profile_tool


registry = ToolRegistry()

registry.register(customer_profile_tool)