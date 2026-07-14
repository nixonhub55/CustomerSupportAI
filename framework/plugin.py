from abc import ABC, abstractmethod


class Plugin(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    def version(self):
        return "1.0"

    @abstractmethod
    def register(self, framework):
        """
        Called when the framework loads the plugin.
        """
        pass