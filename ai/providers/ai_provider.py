from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def ask(self, prompt: str) -> str:
        """
        Send a prompt to the AI and return the response.
        """
        pass