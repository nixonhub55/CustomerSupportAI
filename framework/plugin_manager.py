import importlib
import os


class PluginManager:

    def __init__(self):

        self.plugins = []

    def load_plugins(self, framework):

        plugins_dir = "plugins"

        for folder in os.listdir(plugins_dir):

            path = os.path.join(plugins_dir, folder)

            if not os.path.isdir(path):
                continue

            try:

                module = importlib.import_module(
                    f"plugins.{folder}.plugin"
                )

                plugin = module.Plugin()

                plugin.register(framework)

                self.plugins.append(plugin)

                print(f"Loaded plugin: {plugin.name}")

            except Exception as ex:

                print(f"Failed loading {folder}: {ex}")