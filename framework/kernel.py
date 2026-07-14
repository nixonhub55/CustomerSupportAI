from framework.ai_engine import AIEngine
from framework.tool_registry import ToolRegistry


class Kernel:

    def __init__(self):

        self.tools = ToolRegistry()

        self.ai_engine = AIEngine(
            self.tools
        )


    def boot(self):

        print("AI Framework starting...")

        self.load_tools()

        print("AI Framework ready.")



    def load_tools(self):

        from tools.register import register_tools

        register_tools(
            self.tools
        )