from core.tool import Tool

from services.database_service import get_customer_profile


customer_profile_tool = Tool(

    name="customer_profile",

    description="Retrieve customer profile",

    handler=get_customer_profile

)