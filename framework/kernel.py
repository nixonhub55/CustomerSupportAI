from core.container import Container
from core.logger import Logger

from framework.ai_engine import AIEngine
from framework.tool_registry import ToolRegistry
from framework.conversation_context import ConversationContext

from assistants.billing_assistant import BillingAssistant


class Kernel:

    def __init__(self):

        # -------------------------
        # Infrastructure
        # -------------------------

        self.container = Container()

        self.tools = ToolRegistry()

        self.context = ConversationContext()

        self.assistants = {}

        # -------------------------
        # Register services
        # -------------------------

        self.container.register_factory(
            "ai_engine",
            lambda: AIEngine(
                self.tools,
                self.context
            )
        )

    # -----------------------------------------------------

    def boot(self):

        Logger.info(
            "AI Framework starting..."
        )

        self.load_tools()

        self.load_assistants()

        Logger.info(
            "AI Framework ready."
        )

    # -----------------------------------------------------

    @property
    def ai_engine(self):

        return self.container.resolve(
            "ai_engine"
        )

    # -----------------------------------------------------

    def load_tools(self):

        from tools.register import register_tools

        register_tools(
            self.tools
        )

    # -----------------------------------------------------

    def load_assistants(self):

        self.assistants = {
            "billing": BillingAssistant()
        }

    # -----------------------------------------------------

    def get_assistant(self, name):

        return self.assistants.get(name)

    # -----------------------------------------------------

    def ask(
        self,
        assistant_name,
        question
    ):

        assistant = self.get_assistant(
            assistant_name
        )

        if assistant is None:

            raise Exception(
                f"Assistant '{assistant_name}' not found."
            )

        return self.ai_engine.ask(
            assistant,
            question
        )