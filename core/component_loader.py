import importlib
import inspect
import pkgutil

from core.base_component import BaseComponent


class ComponentLoader:
    """
    Discovers and loads framework components.
    """

    def __init__(self, registry):
        self.registry = registry

    def load_component(self, module_name, class_name):
        """
        Load and register a single component.
        """

        module = importlib.import_module(module_name)

        component_class = getattr(module, class_name)

        if not issubclass(component_class, BaseComponent):
            raise TypeError(
                f"{class_name} is not a BaseComponent."
            )

        component = component_class()

        self.registry.register(component)

        return component

    def load_package(self, package_name):
        """
        Discover and register all auto-registerable
        components inside a package.
        """

        package = importlib.import_module(package_name)

        if not hasattr(package, "__path__"):
            raise ValueError(
                f"{package_name} is not a package."
            )

        loaded = []

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):

            full_module = f"{package_name}.{module_name}"

            try:

                module = importlib.import_module(full_module)

            except Exception as ex:

                print(
                    f"[Loader] Failed importing {full_module}: {ex}"
                )

                continue

            for _, cls in inspect.getmembers(module, inspect.isclass):

                # Ignore imported classes
                if cls.__module__ != module.__name__:
                    continue

                # Must inherit from BaseComponent
                if not issubclass(cls, BaseComponent):
                    continue

                # Don't instantiate BaseComponent itself
                if cls is BaseComponent:
                    continue

                # Skip components that don't opt in
                if not getattr(cls, "AUTO_REGISTER", False):
                    continue

                try:

                    component = cls()

                    self.registry.register(component)

                    loaded.append(
                        component.metadata()["name"]
                    )

                except Exception as ex:

                    print(
                        f"[Loader] Failed loading {cls.__name__}: {ex}"
                    )

        return loaded
