from services.database_service import (
    get_customer_profile,
    format_customer
)

from services.intent_service import detect_intent
from services.knowledge_service import get_knowledge
from services.prompt_service import build_prompt

from ollama_client import generate


def ask(account_no, question):

    # Detect the user's intent
    intent = detect_intent(question)

    # Retrieve customer profile
    customer = get_customer_profile(account_no)

    # Format the customer information
    customer_text = format_customer(customer)

    # Retrieve only the relevant knowledge
    knowledge = get_knowledge(intent)

    # Build the prompt from the template
    prompt = build_prompt(
        "billing_prompt.txt",
        customer_text,
        knowledge,
        question
    )

    # Send to Ollama
    return generate(prompt)