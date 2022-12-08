class Payment:
    def __init__(self, balance, amount):
        self.amount = amount
        self.balance = balance

    def sumer(self):
        if self.balance + self.amount < 0:
            return 'неверная сумма'
        return self.balance + self.amount

    def balanse(self):
        return self.balance

