class RandomizedSet:
# since we need to do in 0(1) just keep tack of the index in a dictionary interstion is nomal
# the challenging part is with the removal part. if you just do pop(index) then all the elements 
# next to the pop elements will move to the left this will miss up our index tracking in the 
# dictonary so instead for removing just swap the going to be removed with the last element of the 
# list and updated the last element index in the dictonary and delete the removed element
# and pop to remove end or swaped element from the list

    def __init__(self):
        self.random = [] 
        self.rand_dict = {}
    def insert(self, val: int) -> bool:
        
        if val not in self.random:
            self.rand_dict[val] = len(self.random)
            self.random.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.random:
            idx = self.rand_dict[val]
            last_val = self.random[-1]
            self.random[idx] = last_val
            self.rand_dict[last_val] = idx
            self.random.pop()
            del self.rand_dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.random)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()