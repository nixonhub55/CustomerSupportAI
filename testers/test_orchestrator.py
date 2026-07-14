from orchestrators.billing_orchestrator import BillingOrchestrator

bot = BillingOrchestrator()

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    print("\nAI:\n")

    print(bot.ask(question))