class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(self, tool):

        self.tools[tool.name] = tool

    def execute(self, name, **kwargs):

        tool = self.tools.get(name)

        if tool is None:

            raise Exception(f"Unknown tool: {name}")

        return tool.execute(**kwargs)