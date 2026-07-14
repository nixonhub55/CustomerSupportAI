from services.billing_service import BillingService

billing = BillingService()

summary = billing.get_customer_summary("100001")

from pprint import pprint

pprint(summary)