from abc import ABC, abstractmethod

from core.base_component import BaseComponent


class BaseWorkflow(BaseComponent, ABC):
    """
    Base class for executable workflows.
    """

    AUTO_REGISTER = False

    CATEGORY = "workflow"

    @abstractmethod
    def run(self, context):
        """
        Execute the workflow.
        """
        pass