from ai.provider_manager import ProviderManager


class AI:

    def __init__(self):
        self.provider = ProviderManager()

    def ask(self, prompt: str) -> str:
        return self.provider.ask(prompt)