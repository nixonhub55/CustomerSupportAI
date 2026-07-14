from framework.kernel import Kernel


kernel = Kernel()

kernel.boot()


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = kernel.ask(
        "billing",
        question
    )

    print("\nAI:", answer)