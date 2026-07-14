class ToolRegistry:

    def __init__(self):

        self.tools = {}


    def register(self, tool):

        self.tools[tool.name] = tool


    def get(self, name):

        return self.tools.get(name)


    def execute(self, name, **kwargs):

        tool = self.get(name)

        if tool is None:

            raise Exception(
                f"Tool '{name}' is not registered."
            )

        return tool.execute(**kwargs)


    def list(self):

        return list(self.tools.keys())