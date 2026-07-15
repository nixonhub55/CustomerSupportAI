class ComponentRegistry:
    """
    Stores and manages framework components.
    """

    def __init__(self):
        self.components = {}

    def register(self, component):
        """
        Register a component.
        """

        name = component.metadata()["name"]

        if not name:
            raise ValueError(
                "Component has no name."
            )

        if name in self.components:
            raise ValueError(
                f"Component '{name}' is already registered."
            )

        self.components[name] = component

    def get(self, name):
        """
        Get a component by name.
        """
        return self.components.get(name)

    def exists(self, name):
        """
        Check whether a component exists.
        """
        return name in self.components

    def list(self):
        """
        Return all registered component names.
        """
        return sorted(self.components.keys())

    def all(self):
        """
        Return all registered component instances.
        """
        return list(self.components.values())

    def clear(self):
        """
        Remove all registered components.
        """
        self.components.clear()