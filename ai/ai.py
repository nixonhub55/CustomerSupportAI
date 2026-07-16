from ai.provider_manager import ProviderManager


class AI:

    def __init__(self):

        self.manager = ProviderManager()

    # -----------------------------------------------------

    def ask(
        self,
        assistant,
        question,
        context=None
    ):

        if context is None:
            context = {}

        prompt = f"""
{assistant.SYSTEM_PROMPT}

Available Tools:
{", ".join(assistant.TOOLS)}

==================================================

Retrieved Context

{context}

==================================================

Customer Question

{question}

==================================================

Instructions

- Answer using ONLY the retrieved context.
- Do not invent customer information.
- If the context does not contain the answer,
  politely say that the information is unavailable.
- Be concise and professional.
"""

        return self.manager.ask(prompt)