from core.logger import Logger


class ContextResolver:

    def __init__(self, conversation_context):
        self.context = conversation_context

    # -------------------------------------------------

    def resolve(self, execution_plan):

        memory = self.context.all()

        if not memory:
            return execution_plan

        Logger.debug(
            f"Resolving using context: {memory}"
        )

        for step in execution_plan.steps:

            arguments = step.get("arguments", {})

            for key, value in arguments.items():

                if value is None and key in memory:

                    arguments[key] = memory[key]

                    Logger.debug(
                        f"Resolved '{key}' from context -> {memory[key]}"
                    )

        return execution_plan