from services.planner_service import plan


class Dispatcher:

    def __init__(self, registry):

        self.registry = registry

    def dispatch(self, assistant, question):

        execution_plan = plan(question)

        context = {}

        for action in execution_plan:

            tool = action["tool"]

            args = action.get("args", {})

            context[tool] = self.registry.execute(
                tool,
                **args
            )

        return context