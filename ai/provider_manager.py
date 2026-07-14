from config import AI_PROVIDER

from ai.providers.ollama_provider import OllamaProvider


class ProviderManager:

    def __init__(self):
        self.provider = self._load_provider()

    def _load_provider(self):

        if AI_PROVIDER.lower() == "ollama":
            return OllamaProvider()

        raise ValueError(
            f"Unsupported AI Provider: {AI_PROVIDER}"
        )

    def ask(self, prompt: str) -> str:
        return self.provider.ask(prompt)