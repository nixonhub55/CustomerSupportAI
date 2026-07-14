from framework.plugin import Plugin as BasePlugin


class Plugin(BasePlugin):

    @property
    def name(self):
        return "Billing"

    @property
    def version(self):
        return "1.0"

    def register(self, framework):

        print("Billing Plugin Loaded")