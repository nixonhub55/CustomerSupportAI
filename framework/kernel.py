from framework.ai_engine import AIEngine
from framework.tool_registry import ToolRegistry
from assistants.billing_assistant import BillingAssistant


class Kernel:

    def __init__(self):

        self.tools = ToolRegistry()
        self.assistants = {}

        self.ai_engine = AIEngine(
            self.tools
        )

    def boot(self):

        print("AI Framework starting...")

        self.load_tools()

        self.load_assistants()

        print("AI Framework ready.")

    def load_tools(self):

        from tools.register import register_tools

        register_tools(
            self.tools
        )

    def load_assistants(self):

        self.assistants = {
            "billing": BillingAssistant()
        }

    def get_assistant(self, name):

        return self.assistants.get(name)

    def ask(self, assistant_name, question):

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