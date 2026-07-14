from ai.provider_manager import ProviderManager


class AI:

    def __init__(self):

        self.manager = ProviderManager()

    def ask(self, question, context=None):

        if context is None:
            context = {}

        prompt = f"""
You are a helpful customer support AI.

Context:
{context}

Customer Question:
{question}

Answer the customer's question using the provided context. If the context is insufficient, say so politely.
"""

        return self.manager.ask(prompt)