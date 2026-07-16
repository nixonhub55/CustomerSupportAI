from core.logger import Logger


class Dispatcher:

    def __init__(self, registry):

        self.registry = registry

    def dispatch(self, execution_plan):

        context = {}

        for step in execution_plan.steps:

            tool = step["tool"]
            arguments = step["arguments"]

            Logger.info(
                f"Dispatching tool: {tool}"
            )

            Logger.debug(
                f"Arguments: {arguments}"
            )

            context[tool] = self.registry.execute(
                tool,
                **arguments
            )

        return context