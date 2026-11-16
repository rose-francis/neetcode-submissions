from random import choice
class RandomizedSet:

    def __init__(self):
        self.items=[]

    def insert(self, val: int) -> bool:
        if val not in self.items:
            self.items.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.items:
            self.items.remove(val)

    def getRandom(self) -> int:
        return choice(self.items)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()