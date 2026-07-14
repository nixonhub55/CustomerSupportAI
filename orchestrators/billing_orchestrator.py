from memory.session import session
from services.logger_service import logger
from services.planner_service import plan
from services.context_service import build_context
from services.response_service import generate_response


class BillingOrchestrator:

    def ask(self, question):

        action = plan(question)

        if action["account_no"]:
            session.set_customer(action["account_no"])

        elif action["customer"]:
            action["account_no"] = session.get_customer()

        context = build_context(
            action,
            question
        )

        answer = generate_response(
            question,
            context
        )

        session.add_message(
            "user",
            question
        )

        session.add_message(
            "assistant",
            answer
        )

        """ Insert Logger """
        logger.info(f"Question: {question}") 
        action = plan(question) 
        logger.info(f"Intent: {action['intent']}")

        return answer