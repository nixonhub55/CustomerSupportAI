from database.repositories.base_repository import BaseRepository


class CustomerRepository(BaseRepository):

    TABLE = "customers"

    PRIMARY_KEY = "account_no"

    DISPLAY_NAME = "Customer"

    DESCRIPTION = "Customer account information."

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