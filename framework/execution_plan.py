class ExecutionPlan:
    """
    Represents a list of tool execution steps.
    """

    def __init__(self):

        self.steps = []

    # -----------------------------------------------------

    def add(
        self,
        tool,
        **arguments
    ):

        self.steps.append({
            "tool": tool,
            "arguments": arguments
        })

    # -----------------------------------------------------

    def empty(self):

        return len(self.steps) == 0

    # -----------------------------------------------------

    def to_dict(self):

        return {
            "steps": self.steps
        }