class EventBus:
    """
    Simple publish/subscribe event bus.
    """

    def __init__(self):

        self._listeners = {}

    # -------------------------

    def subscribe(
        self,
        event,
        handler
    ):

        self._listeners.setdefault(
            event,
            []
        ).append(handler)

    # -------------------------

    def publish(
        self,
        event,
        payload=None
    ):

        for handler in self._listeners.get(
            event,
            []
        ):

            handler(payload)

    # -------------------------

    def listeners(
        self,
        event
    ):

        return self._listeners.get(
            event,
            []
        )

    # -------------------------

    def clear(self):

        self._listeners.clear()