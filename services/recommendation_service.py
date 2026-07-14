from dataclasses import dataclass, field


@dataclass
class RecommendationService:

    def analyze(self, customer):

        recommendations = []

        if customer["balance"] > 0:

            recommendations.append(

                "Customer has an outstanding balance."

            )

        if len(customer["unpaid_invoices"]):

            recommendations.append(

                "Customer has unpaid invoices."

            )

        if len(customer["open_tickets"]):

            recommendations.append(

                "Customer has open support tickets."

            )

        if len(customer["pending_requests"]):

            recommendations.append(

                "Customer has pending service requests."

            )

        if not recommendations:

            recommendations.append(

                "Customer account looks healthy."

            )

        return recommendations