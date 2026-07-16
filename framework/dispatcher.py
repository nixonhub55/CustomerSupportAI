class Dispatcher:

    def __init__(self, registry):

        self.registry = registry

    # -----------------------------------------------------

    def dispatch(
        self,
        assistant,
        question
    ):

        from services.planner_service import plan

        execution_plan = plan(question)

        context = {}

        for step in execution_plan.steps:

            tool = step["tool"]

            if tool not in assistant.TOOLS:

                raise PermissionError(
                    f"{assistant.name} cannot use '{tool}'."
                )

            arguments = step["arguments"]

            context[tool] = self.registry.execute(
                tool,
                **arguments
            )

        return context