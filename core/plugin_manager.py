class PluginManager:

    def __init__(self):

        self._plugins = {}

    def register(self, plugin):

        self._plugins[
            plugin.metadata()["name"]
        ] = plugin

    def get(self, name):

        return self._plugins.get(name)

    def list(self):

        return sorted(
            self._plugins.keys()
        )

    def start_all(self):

        for plugin in self._plugins.values():

            plugin.start()

    def stop_all(self):

        for plugin in self._plugins.values():

            plugin.stop()