from database.repositories.base_repository import BaseRepository


class CustomerRepository(BaseRepository):

    TABLE = "customers"

    PRIMARY_KEY = "account_no"

    NAME = "customer"

    DISPLAY_NAME = "Customer"

    DESCRIPTION = "Customer account information."

    CATEGORY = "repository"

    VERSION = "1.0.0"

    DEFAULT_ORDER = "lastname"

    SEARCHABLE_FIELDS = {
        "account_no",
        "phone",
        "email",
        "firstname",
        "lastname",
        "middlename",
        "status",
        "plan"
    }