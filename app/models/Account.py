class Account:
    def __init__(self, id: int, user_id: int, balance: float, currency: str, is_active: bool = True):
        self.id = id
        self.user_id = user_id  
        self.balance = balance
        self.currency = currency
        self.is_active = is_active
