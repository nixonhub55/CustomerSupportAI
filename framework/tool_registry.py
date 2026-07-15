class ToolRegistry:
    """
    Registry for all framework tools.
    """

    def __init__(self):

        self.tools = {}

    # -----------------------------------------------------

    def register(self, tool): 
        
        print("=" * 60)
        print("Class:", tool.__class__.__name__)
        print("Metadata:", tool.metadata())
        print("=" * 60)

        metadata = tool.metadata()

        name = metadata.get("name")

        if not name:
            raise ValueError(
                f"{tool.__class__.__name__} has no NAME defined."
            )

        self.tools[name] = tool
    # -----------------------------------------------------

    def get(self, name):
        """
        Return a tool instance.
        """

        return self.tools.get(name)

    # -----------------------------------------------------

    def execute(self, name, **kwargs):
        """
        Execute a registered tool.
        """

        tool = self.get(name)

        if tool is None:
            raise ValueError(
                f"Tool '{name}' is not registered."
            )

        return tool.execute(**kwargs)

    # -----------------------------------------------------

    def exists(self, name):
        """
        Check whether a tool exists.
        """

        return name in self.tools

    # -----------------------------------------------------

    def list(self):
        """
        Return all tool names.
        """

        return sorted(self.tools.keys())

    # -----------------------------------------------------

    def metadata(self):
        """
        Return metadata for all registered tools.
        """

        return [
            tool.metadata()
            for tool in self.tools.values()
        ]

    # -----------------------------------------------------

    def clear(self):
        """
        Remove all registered tools.
        """

        self.tools.clear()