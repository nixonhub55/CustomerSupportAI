from core.logger import Logger

from framework.dispatcher import Dispatcher
from ai.ai import AI
from services.context_resolver import ContextResolver
from services.planner_service import plan
from services.plan_validator import validate
from services.context_manager import ContextManager
from services.conversation_resolver import ConversationResolver
from services.result_processor import ResultProcessor


class AIEngine:

    def __init__(self, registry, context):

        Logger.info("Creating AI Engine") 

        self.dispatcher = Dispatcher(registry)  
        self.ai = AI()

        self.context = context

        self.conversation_resolver = ConversationResolver(
            self.context
        )

        self.context_manager = ContextManager(context)

        self.context_resolver = ContextResolver(
            context
        )

        self.result_processor = ResultProcessor()

    # -------------------------------------------------

    def ask(self, assistant, question):

        Logger.info(
            f"Assistant: {assistant.NAME}"
        )

        Logger.info(
            f"Question: {question}"
        )

        # -------------------------------------------------
        # Planning
        # -------------------------------------------------

        question = self.conversation_resolver.resolve(
            question
        )

        execution_plan = plan(question)

        Logger.info(
            f"Intent: {execution_plan.intent}"
        )

        Logger.debug(
            f"Question after conversation resolver: {question}"
        )

        execution_plan = self.context_resolver.resolve(
            execution_plan
        )

        errors = validate(execution_plan)

        if errors:

            Logger.warning(
                f"Validation failed: {errors}"
            )

            return "\n".join(errors)

        # -------------------------------------------------
        # Execute Tools
        # -------------------------------------------------

        raw_context = self.dispatcher.dispatch(
            execution_plan
        )

        context = self.result_processor.process(
            raw_context
        )

        # -------------------------------------------------
        # Update Conversation Context
        # -------------------------------------------------

        entities = {}

        for step in execution_plan.steps:

            entities.update(
                step.get("arguments", {})
            )

        self.context_manager.update(
            entities
        )

        Logger.debug(
            f"Conversation Context: {self.context.all()}"
        )

        # -------------------------------------------------
        # Ask AI
        # -------------------------------------------------

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