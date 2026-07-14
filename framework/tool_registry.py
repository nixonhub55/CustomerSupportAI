class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(self, tool):
        """
        Register a tool instance.
        """

        self.tools[tool.name] = tool

    def execute(self, tool_name, **kwargs):
        """
        Execute a registered tool.
        """

        tool = self.tools.get(tool_name)

        if tool is None:
            raise Exception(
                f"Tool '{tool_name}' is not registered."
            )

        return tool.execute(**kwargs)

    def get(self, tool_name):
        """
        Return a tool instance.
        """

        return self.tools.get(tool_name)

    def exists(self, tool_name):
        """
        Check if a tool exists.
        """

        return tool_name in self.tools

    def list(self):
        """
        Return all registered tool names.
        """

        return sorted(self.tools.keys())