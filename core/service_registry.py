class ServiceRegistry:
    """
    Registry for framework services.
    """

    def __init__(self):
        self._services = {}

    def add(self, name, instance):

        if name in self._services:
            raise ValueError(
                f"Service '{name}' already exists."
            )

        self._services[name] = instance

    def get(self, name):

        return self._services.get(name)

    def exists(self, name):

        return name in self._services

    def remove(self, name):

        self._services.pop(name, None)

    def clear(self):

        self._services.clear()

    def list(self):

        return sorted(self._services.keys())