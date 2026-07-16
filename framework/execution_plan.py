class ExecutionPlan:

    def __init__(self):

        self.intent = "unknown"

        self.requires_context = False

        self.steps = []

    # -----------------------------------------------------

    def add_step(
        self,
        tool,
        **arguments
    ):

        self.steps.append({

            "tool": tool,

            "arguments": arguments
        })

        self.requires_context = True

    # -----------------------------------------------------

    def is_empty(self):

        return len(self.steps) == 0

    # -----------------------------------------------------

    def to_dict(self):

        return {

            "intent": self.intent,

            "requires_context": self.requires_context,

            "steps": self.steps
        }