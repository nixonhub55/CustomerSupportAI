from services.planner_service import plan

execution_plan = plan(
    "Show customer 100001"
)
print(execution_plan.to_dict())