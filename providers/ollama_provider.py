from providers.ai_provider import AIProvider

from ollama_client import generate


class OllamaProvider(AIProvider):

    def generate(self, prompt):

        return generate(prompt)


        