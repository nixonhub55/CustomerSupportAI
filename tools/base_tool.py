from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for all framework tools.
    """

    name = ""

    description = ""

    category = "general"

    parameters = []

    plugin = "core"

    def metadata(self):

        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "plugin": self.plugin,
            "parameters": self.parameters
        }

    @abstractmethod
    def execute(self, **kwargs):
        pass