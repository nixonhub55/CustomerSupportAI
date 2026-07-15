class WorkflowManager:

    def __init__(self):

        self._workflows = {}

    def register(self, workflow):

        self._workflows[
            workflow.metadata()["name"]
        ] = workflow

    def get(self, name):

        return self._workflows.get(name)

    def exists(self, name):

        return name in self._workflows

    def list(self):

        return sorted(
            self._workflows.keys()
        )

    def execute(
        self,
        name,
        context
    ):

        workflow = self.get(name)

        if workflow is None:

            raise ValueError(
                f"Workflow '{name}' not found."
            )

        return workflow.run(context)