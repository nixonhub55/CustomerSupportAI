from framework.dispatcher import Dispatcher

from ai.ai import AI


class AIEngine:

    def __init__(self):

        self.dispatcher = Dispatcher()

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