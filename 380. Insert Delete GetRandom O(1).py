from random import choice


class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val not in self.val_to_idx:
            self.vals.append(val)
            self.val_to_idx[val] = len(self.vals) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_to_idx:
            idx = self.val_to_idx[val]
            self.vals[idx], self.vals[-1] = self.vals[-1], self.vals[idx]
            self.val_to_idx[self.vals[idx]] = idx
            self.vals.pop()
            del self.val_to_idx[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.vals)
