from typing import List


class ATM:

    def __init__(self):
        self.denomination = [0, 0, 0, 0, 0]
        self.order = [500, 200, 100, 50, 20]

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx, banknote in enumerate(banknotesCount):
            self.denomination[idx] += banknote

    def withdraw(self, amount: int) -> List[int]:
        ans = [0, 0, 0, 0, 0]
        for idx, banknote in enumerate(self.order):
            if amount > 0:
                i = len(ans) - idx - 1
                quantity = amount // banknote
                quantity = min(quantity, self.denomination[i])
                amount -= quantity * banknote
                ans[i] = quantity

        if amount > 0:
            return [-1, ]

        for idx, q in enumerate(ans):
            self.denomination[idx] -= q
        return ans