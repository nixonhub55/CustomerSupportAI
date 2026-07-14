from core.tool import Tool


class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(self, tool):

        self.tools[tool.name] = tool

    def execute(self, name, *args, **kwargs):

        tool = self.tools.get(name)

        if tool is None:

            raise Exception(
                f"Tool '{name}' not found."
            )

        return tool.handler(*args, **kwargs)

    def list_tools(self):

        return list(self.tools.keys())