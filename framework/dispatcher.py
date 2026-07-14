from services.planner_service import plan


class Dispatcher:


    def __init__(self, registry):

        self.registry = registry


    def dispatch(
        self,
        assistant,
        question
    ):

        execution_plan = plan(question)

        context = {}

        for task in execution_plan:

            result = self.registry.execute(
                task["tool"],
                task.get("args", {})
            )

            context[task["tool"]] = result


        return context