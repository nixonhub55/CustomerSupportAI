from abc import ABC, abstractmethod

from core.base_component import BaseComponent


class BaseTool(BaseComponent, ABC):
    """
    Base class for all framework tools.
    """

    AUTO_REGISTER = False

    NAME = ""

    DISPLAY_NAME = ""

    DESCRIPTION = ""

    CATEGORY = "general"

    PARAMETERS = []

    PLUGIN = "core"

    def metadata(self):

        data = super().metadata()

        data.update({

            "plugin": self.PLUGIN,

            "parameters": self.PARAMETERS,

            "keywords": getattr(
                self,
                "KEYWORDS",
                []
            ),

            "examples": getattr(
                self,
                "EXAMPLES",
                []
            )

        })

        return data

    @abstractmethod
    def execute(self, **kwargs):
        pass