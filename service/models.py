class Account:
    """Account Model"""

    accounts = []

    def __init__(self, name, email):
        self.id = len(Account.accounts) + 1
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
