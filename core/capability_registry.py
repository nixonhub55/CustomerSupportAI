class CapabilityRegistry:
    """
    Stores all business capabilities.
    """

    def __init__(self):

        self._capabilities = []

    def register(self, capability):

        self._capabilities.append(capability)

    def all(self):

        return self._capabilities

    def clear(self):

        self._capabilities.clear()

    def count(self):

        return len(self._capabilities)