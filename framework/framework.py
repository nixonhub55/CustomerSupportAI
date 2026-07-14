from framework.tool_manager import ToolManager
from framework.agent_manager import AgentManager
from framework.plugin_manager import PluginManager
from framework.dispatcher import ToolDispatcher

class Framework:

    def __init__(self):
        
        self.dispatcher = ToolDispatcher(self)

        self.tools = ToolManager()

        self.agents = AgentManager()

        self.plugin_manager = PluginManager()

    def start(self):

        self.plugin_manager.load_plugins(self)

    def info(self):

        print()

        print("========== NixAI Framework ==========")

        print()

        print("Loaded Plugins:")

        for plugin in self.plugin_manager.plugins:

            print(
                f" - {plugin.name} ({plugin.version})"
            )

        print()

        print("Registered Agents:")

        for agent in self.agents.list():

            print(
                f" - {agent}"
            )

        print()

        print("Registered Tools:")

        for tool in self.tools.list():

            print(
                f" - {tool}"
            )