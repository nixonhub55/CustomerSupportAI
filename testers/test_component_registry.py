from core.component_registry import ComponentRegistry
from core.component_loader import ComponentLoader

registry = ComponentRegistry()
loader = ComponentLoader(registry)

loaded = loader.load_package("tools")
