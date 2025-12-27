class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.res = {}

    def insert(self, val: int) -> bool:
        if val not in self.res:
            n = len(self.arr)
            self.res[val] = n 
            self.arr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.res:
            i = self.res[val]
            last_val = self.arr[-1]

            self.arr[i] = last_val
            self.res[last_val] = i
            self.arr.pop()
            self.res.pop(val)
            
            

            return True
        else:
            return False   

    def getRandom(self) -> int:
        a = random.choice(self.arr)

        return a


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()