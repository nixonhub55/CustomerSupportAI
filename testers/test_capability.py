from core.component_loader import ComponentLoader
from core.workflow_manager import WorkflowManager

manager = WorkflowManager()

loader = ComponentLoader(manager)

loader.load_package(
    "workflows"
)

print(manager.list())

manager.execute(
    "customer_summary",
    {}
)