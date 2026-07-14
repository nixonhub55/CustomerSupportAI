import requests

from config import *

from ai.providers.ai_provider import AIProvider
from services.logger_service import logger
import time


class OllamaProvider(AIProvider):

    def ask(self, prompt):

    start = time.time()

    response = requests.post(
        ...
    )

    elapsed = time.time() - start

    logger.info(
        f"Ollama ({AI_MODEL}) responded in {elapsed:.2f} seconds."
    )

    return response.json()["response"]