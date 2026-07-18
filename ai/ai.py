import json

from ai.provider_manager import ProviderManager
from core.logger import Logger


class AI:

    def __init__(self):

        self.manager = ProviderManager()

    # -----------------------------------------------------

    def ask(
        self,
        assistant,
        question,
        execution_plan,
        context
    ):

        context_json = json.dumps(
            context,
            indent=2,
            default=str
        )

        prompt = f"""
{assistant.SYSTEM_PROMPT}

==================================================
EXECUTION RESULT
==================================================

The backend has already executed all required tools.

The following JSON is the ONLY source of truth.

If the JSON contains the answer, use it.

Do NOT ignore it.

Do NOT ask the user to verify information that already exists.

Do NOT request an account number if one is already present.

Do NOT request identity verification.

Do NOT mention social security numbers.

Do NOT invent data.

If the context is empty, say that no information was found.

==================================================
INTENT
==================================================

{execution_plan.intent}

==================================================
TOOL RESULTS
==================================================

{context_json}

==================================================
USER QUESTION
==================================================

{question}

==================================================
YOUR TASK
==================================================

Answer ONLY from the tool results.

If multiple tools were executed, combine their information naturally.

Keep the answer short, accurate, and professional.
"""

        Logger.debug(prompt)

        return self.manager.ask(prompt)