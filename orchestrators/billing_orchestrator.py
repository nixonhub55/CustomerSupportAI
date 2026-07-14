from framework.agents.base_agent import BaseAgent

from orchestrators.billing_orchestrator import BillingOrchestrator


class BillingAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.orchestrator = BillingOrchestrator()

    def ask(self, question):

        return self.orchestrator.ask(question)

    def plan(self, question):
        pass

    def execute(self, action):
        pass

    def respond(self, question, context):
        pass