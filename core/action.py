from dataclasses import dataclass, field


@dataclass
class Action:

    def __init__(

        self,

        intent,

        account_no=None,

        customer=False,

        knowledge=False,

        entities=None

    ):

        self.intent = intent

        self.account_no = account_no

        self.customer = customer

        self.knowledge = knowledge

        self.entities = entities or {}