from ai.provider_manager import ProviderManager


class AI:

    def __init__(self):

        self.manager = ProviderManager()

    def ask(self, prompt):

        return self.manager.ask(prompt)