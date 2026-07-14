from abc import ABC, abstractmethod


class BaseAgent(ABC):

    def __init__(self, framework=None):

        self.framework = framework

    def ask(self, question):

        action = self.plan(question)

        context = self.execute(action)

        return self.respond(question, context)

    @abstractmethod
    def plan(self, question):
        pass

    @abstractmethod
    def execute(self, action):
        pass

    @abstractmethod
    def respond(self, question, context):
        pass