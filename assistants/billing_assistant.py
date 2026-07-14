class BillingAssistant:


    def __init__(
        self,
        engine
    ):

        self.engine = engine



    def ask(
        self,
        question
    ):

        return self.engine.ask(
            "billing",
            question
        )