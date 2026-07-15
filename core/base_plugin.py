from abc import ABC

from core.base_component import BaseComponent


class BasePlugin(BaseComponent, ABC):
    """
    Base class for framework plugins.
    """

    AUTO_REGISTER = False

    CATEGORY = "plugin"

    VERSION = "1.0.0"

    AUTHOR = ""

    TAGS = []

    ENABLED = True

    def start(self):
        """
        Called when the plugin is loaded.
        """
        pass

    def stop(self):
        """
        Called when the plugin is unloaded.
        """
        pass