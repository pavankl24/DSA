class ATM(object):

    def __init__(self):
        self.counts = [0] * 5
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        for i in range(5):
            self.counts[i] += banknotesCount[i]

    def withdraw(self, amount):
        take = [0] * 5
        for i in range(4, -1, -1):
            val = self.values[i]
            cnt = amount // val
            actual = min(cnt, self.counts[i])
            take[i] = actual
            amount -= actual * val
            
        if amount == 0:
            for i in range(5):
                self.counts[i] -= take[i]
            return take
        return [-1]
