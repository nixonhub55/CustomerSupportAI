from dataclasses import dataclass, field


@dataclass
class ExecutionPlan:

    def __init__(self):

        self.actions = []

    def add(self, action):

        self.actions.append(action)