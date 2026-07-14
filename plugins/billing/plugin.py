from framework.plugin import Plugin as BasePlugin

from plugins.billing.tools import register_tools


class Plugin(BasePlugin):

    @property
    def name(self):
        return "Billing"

    @property
    def version(self):
        return "1.0"

    def register(self, framework):

        register_tools(framework)

        print("Billing Plugin Loaded")