class Lifecycle:
    """
    Coordinates framework startup and shutdown.
    """

    def __init__(self):

        self._startup = []
        self._shutdown = []

    # -------------------------

    def on_startup(self, handler):

        self._startup.append(handler)

    # -------------------------

    def on_shutdown(self, handler):

        self._shutdown.append(handler)

    # -------------------------

    def startup(self):

        for handler in self._startup:

            handler()

    # -------------------------

    def shutdown(self):

        for handler in reversed(self._shutdown):

            handler()