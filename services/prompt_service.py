import os

PROMPT_FOLDER = "prompts"


def load_template(filename):

    path = os.path.join(PROMPT_FOLDER, filename)

    with open(path, "r", encoding="utf-8") as file:

        return file.read()


def build_prompt(template_name, customer, knowledge, question):

    prompt = load_template(template_name)

    prompt = prompt.replace(
        "{{customer}}",
        customer
    )

    prompt = prompt.replace(
        "{{knowledge}}",
        knowledge
    )

    prompt = prompt.replace(
        "{{question}}",
        question
    )

    return prompt