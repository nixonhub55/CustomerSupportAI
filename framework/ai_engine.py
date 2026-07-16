from core.logger import Logger

from framework.dispatcher import Dispatcher
from ai.ai import AI
from services.planner_service import plan


class AIEngine:

    def __init__(self, registry):

        Logger.info("Creating AI Engine")

        self.dispatcher = Dispatcher(registry)
        self.ai = AI()

    def ask(self, assistant, question):

        Logger.info(
            f"Assistant: {assistant.NAME}"
        )

        Logger.info(
            f"Question: {question}"
        )

        execution_plan = plan(question)

        Logger.info(
            f"Intent: {execution_plan.intent}"
        )

        context = self.dispatcher.dispatch(
            execution_plan
        )

        Logger.info(
            "Sending prompt to AI..."
        )

        answer = self.ai.ask(
            assistant,
            question,
            execution_plan,
            context
        )

        Logger.info(
            "AI response generated."
        )

        return answer