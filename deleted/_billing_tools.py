from services.database_service import get_customer_profile
from services.knowledge_service import get_knowledge


TOOLS = {

    "customer_profile": get_customer_profile,

    "knowledge": get_knowledge,

}