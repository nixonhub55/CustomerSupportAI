class ToolManager:

    def __init__(self):

        self.tools = {}

    def register(self, name, handler, description=""):

        self.tools[name] = {
            "handler": handler,
            "description": description
        }

        print(f"Registered Tool: {name}")

    def execute(self, name, *args, **kwargs):

        if name not in self.tools:
            raise Exception(f"Unknown Tool: {name}")

        return self.tools[name]["handler"](
            *args,
            **kwargs
        )

    def get(self, name):

        return self.tools.get(name)

    def list(self):

        return sorted(self.tools.keys())