from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for all tools.
    """

    name = ""
    description = ""

    @abstractmethod
    def execute(self, **kwargs):
        """
        Execute the tool.
        """
        pass