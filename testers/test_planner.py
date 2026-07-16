from services.planner_service import plan

tests = [
    "Show customer 100001",
    "Show payment history for account 100001",
    "Show unpaid invoices for account 100001",
    "Show tickets for account 100001",
    "How many customers do you have?",
    "Show customer 100001 with payment history and unpaid invoices"
]

for question in tests:

    plan_result = plan(question)

    print("=" * 60)
    print(question)
    print(plan_result.to_dict())