from framework.tool_registry import ToolRegistry
from tools.register import register_tools

registry = ToolRegistry()

register_tools(registry)

from pprint import pprint

pprint(registry.list())