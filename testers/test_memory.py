from memory.session import session

session.add_message(
    "user",
    "Show customer 100001"
)

session.add_message(
    "assistant",
    "Customer loaded."
)

print(session.get_history())