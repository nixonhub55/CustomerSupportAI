from services.billing_service import BillingService

from services.formatter_service import format_customer_summary

billing = BillingService()

summary = billing.get_customer_summary("100001")

print(
    format_customer_summary(summary)
)