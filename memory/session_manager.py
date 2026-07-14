class SessionManager:

    def __init__(self):

        self.current_customer = None

        self.history = []

    def set_customer(self, account_no):

        self.current_customer = account_no

    def get_customer(self):

        return self.current_customer

    def add_message(self, role, message):

        self.history.append({
            "role": role,
            "message": message
        })

    def get_history(self):

        return self.history

    def clear(self):

        self.current_customer = None
        self.history = []