from services.database_service import get_customer_profile


def register_tools(framework):

    framework.tools.register(

        "customer.profile",

        get_customer_profile,

        "Retrieve customer profile by account number."

    )