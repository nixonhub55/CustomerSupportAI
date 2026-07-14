from memory.session import session
from services.planner_service import plan 

print("=" * 50)
print("Billing AI Assistant")
print("=" * 50)

while True:

    question = input("\nYou: ")
    action = plan(question)
    

    if question.lower() == "exit":
        break

    if question.lower() == "clear":
        session.clear()
        print("\nAI: Session cleared.")
        continue

    
        
    print(action)
    print("\nAI: (processing...)")