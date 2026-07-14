import requests
import time

from config import *

from ai.providers.ai_provider import AIProvider
from services.logger_service import logger


class OllamaProvider(AIProvider):

    def ask(self, prompt):

        start = time.time()

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": AI_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        elapsed = time.time() - start

        logger.info(
            f"Ollama ({AI_MODEL}) responded in {elapsed:.2f} seconds."
        )

        return response.json()["response"]