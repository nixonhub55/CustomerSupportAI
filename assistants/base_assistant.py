from core.base_component import BaseComponent


class BaseAssistant(BaseComponent):

    NAME = ""

    DISPLAY_NAME = ""

    DESCRIPTION = ""

    CATEGORY = "assistant"

    PLUGIN = "core"

    SYSTEM_PROMPT = ""

    TOOLS = []

    def metadata(self):

        data = super().metadata()

        data.update({

            "plugin": self.PLUGIN,

            "tools": self.TOOLS
        })

        return data