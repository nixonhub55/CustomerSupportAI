class Memory:
    """
    Short-term conversational memory.
    """

    def __init__(self):

        self.clear()

    # -------------------------

    def remember(self, key, value):

        self._memory[key] = value

    # -------------------------

    def recall(self, key, default=None):

        return self._memory.get(
            key,
            default
        )

    # -------------------------

    def forget(self, key):

        self._memory.pop(
            key,
            None
        )

    # -------------------------

    def clear(self):

        self._memory = {}

    # -------------------------

    def exists(self, key):

        return key in self._memory

    # -------------------------

    def all(self):

        return dict(self._memory)

    # -------------------------

    def __repr__(self):

        return repr(self._memory)