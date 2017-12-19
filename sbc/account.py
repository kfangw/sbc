from uuid import uuid4


class Account:
    def __init__(self):
        self.address = str(uuid4()).replace('-', '')
        self.balance = 0


class TCAccount(Account):
    def __init__(self):
        super().__init__()
        self.values = {}


class UserAccount(Account):
    def __init__(self):
        super().__init__()

