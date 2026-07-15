from abc import ABC, abstractmethod

from core.base_component import BaseComponent


class BaseCapability(BaseComponent, ABC):
    """
    Base class for all business capabilities.
    """

    AUTO_REGISTER = False

    NAME = ""

    DISPLAY_NAME = ""

    DESCRIPTION = ""

    CATEGORY = "capability"

    VERSION = "1.0.0"

    AUTHOR = ""

    TAGS = []

    @abstractmethod
    def can_handle(self, plan):
        """
        Return True if this capability
        can process the execution plan.
        """
        pass

    @abstractmethod
    def execute(self, plan):
        """
        Execute the capability.
        """
        pass