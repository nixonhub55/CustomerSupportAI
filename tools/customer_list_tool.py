from core.base_component import BaseComponent

from services.customer_list_service import (
    get_customer_list
)


class CustomerListTool(BaseComponent):

    NAME = "customer_list"

    DISPLAY_NAME = "Customer List"

    DESCRIPTION = "Returns a list of customers."

    CATEGORY = "tool"

    VERSION = "1.0.0"

    def execute(self, **kwargs):

        return get_customer_list(**kwargs)