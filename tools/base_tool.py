from abc import ABC, abstractmethod


class BaseTool(ABC):

    @property
    def name(self):
        """
        Automatically derive the tool name from the class name.
        Example:
            CustomerLookupTool -> customer_lookup
        """
        name = self.__class__.__name__

        name = name.replace("Tool", "")

        words = []

        current = ""

        for c in name:

            if c.isupper() and current:

                words.append(current.lower())

                current = c

            else:

                current += c

        words.append(current.lower())

        return "_".join(words)


    @abstractmethod
    def execute(self, **kwargs):
        pass