from services.prompt_service import build_prompt

from ai.client import AI

ai = AI()


def generate_response(question, context):

    prompt = build_prompt(
        "billing_prompt.txt",
        context["customer_text"],
        context["knowledge"],
        question
    )

    return ai.ask(prompt)