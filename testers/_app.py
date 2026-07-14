from assistants.billing_assistant import ask

account = input("Account Number: ")
question = input("Question: ")

print("\nThinking...\n")

answer = ask(account, question)

print(answer)