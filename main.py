from framework.kernel import Kernel
from assistants.billing_assistant import BillingAssistant



kernel = Kernel()

kernel.boot()



assistant = BillingAssistant(
    kernel.ai_engine
)



while True:

    question = input(
        "\nYou: "
    )


    if question.lower() == "exit":
        break


    answer = assistant.ask(
        question
    )


    print(
        "\nAI:",
        answer
    )