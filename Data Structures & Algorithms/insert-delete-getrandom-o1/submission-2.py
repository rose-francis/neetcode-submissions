from random import choice
class RandomizedSet:

    def __init__(self):
        self.items={}
        self.l=[]

    def insert(self, val: int) -> bool:
        if val not in self.items:
            self.items[val]=len(self.l)
            self.l.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.items:
            idx=self.items[val]
            last=self.l[-1]
            self.l[-1]=self.l[idx]
            self.l[idx]=last
            self.l.pop()
            self.items[last]=idx
            del self.items[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()