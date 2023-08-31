from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        self.sum = 0
        for value in self.data:
            if value > 0:
                self.sum = self.sum + value
        return self.sum