import inspect


class Container:

    def __init__(self):

        self._instances = {}
        self._factories = {}

    # -------------------------------------------------

    def register_instance(self, key, instance):

        self._instances[key] = instance

    # -------------------------------------------------

    def register_factory(self, key, factory):

        self._factories[key] = factory

    # -------------------------------------------------

    def resolve(self, target):

        # Existing singleton

        if target in self._instances:
            return self._instances[target]

        # Existing factory

        if target in self._factories:

            instance = self._factories[target]()

            self._instances[target] = instance

            return instance

        # Automatic construction

        if inspect.isclass(target):

            return self._build(target)

        raise KeyError(
            f"Cannot resolve '{target}'."
        )

    # -------------------------------------------------

    def _build(self, cls):

        signature = inspect.signature(
            cls.__init__
        )

        kwargs = {}

        for name, parameter in list(
            signature.parameters.items()
        )[1:]:

            dependency = parameter.annotation

            if dependency is inspect.Parameter.empty:

                raise TypeError(
                    f"{cls.__name__}.{name} has no type annotation."
                )

            kwargs[name] = self.resolve(
                dependency
            )

        instance = cls(**kwargs)

        self._instances[cls] = instance

        return instance