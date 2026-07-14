from framework.tool_registry import ToolRegistry
from tools.register import register_tools

registry = ToolRegistry()

register_tools(registry)

print(registry.list())