class Context:
    """
    Shared execution context.
    """

    def __init__(self):

        self._data = {}

    # -------------------------

    def set(self, key, value):

        self._data[key] = value

    # -------------------------

    def get(self, key, default=None):

        return self._data.get(
            key,
            default
        )

    # -------------------------

    def exists(self, key):

        return key in self._data

    # -------------------------

    def remove(self, key):

        self._data.pop(key, None)

    # -------------------------

    def clear(self):

        self._data.clear()

    # -------------------------

    def to_dict(self):

        return dict(self._data)

    # -------------------------

    def __getitem__(self, key):

        return self.get(key)

    def __setitem__(self, key, value):

        self.set(key, value)

    def __contains__(self, key):

        return self.exists(key)

    def __repr__(self):

        return repr(self._data)