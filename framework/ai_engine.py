from framework.dispatcher import Dispatcher
from ai.ai import AI


class AIEngine:


    def __init__(self, registry):

        self.ai = AI()

        self.dispatcher = Dispatcher(
            registry
        )


    def ask(
        self,
        assistant,
        question
    ):

        context = self.dispatcher.dispatch(
            assistant,
            question
        )

        return self.ai.ask(
            question,
            context
        )