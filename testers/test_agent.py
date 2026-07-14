from apps.billing.agents.billing_agent import BillingAgent


agent = BillingAgent()

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    print()

    print(agent.ask(question))

    print()