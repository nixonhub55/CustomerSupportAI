from config import AI_PROVIDER

from providers.ollama_provider import OllamaProvider
from providers.openai_provider import OpenAIProvider
from providers.gemini_provider import GeminiProvider


class ProviderManager:

    def __init__(self):

        if AI_PROVIDER == "ollama":
            self.provider = OllamaProvider()

        elif AI_PROVIDER == "openai":
            self.provider = OpenAIProvider()

        elif AI_PROVIDER == "gemini":
            self.provider = GeminiProvider()

        else:
            raise ValueError(f"Unsupported AI provider: {AI_PROVIDER}")

    def generate(self, prompt):

        return self.provider.generate(prompt)