from framework.dispatcher import Dispatcher
from ai.ai import AI


class AIEngine:

    def __init__(self, registry):

        self.dispatcher = Dispatcher(registry)
        self.ai = AI()

    def ask(self, assistant, question):

        context = self.dispatcher.dispatch(
            assistant,
            question
        )

        return self.ai.ask(
            question,
            context
        )